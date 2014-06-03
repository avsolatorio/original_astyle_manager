#-------------------------------------------------------------------------------
# Name:        MainApplication
# Purpose:
#
# Author:      avsolatorio
#
# Created:     03/06/2014
# Copyright:   (c) avsolatorio 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import wx
import wx.html
import difflib
import shutil
import os
import subprocess
import time
from AStyleToolModules.AStyleDiffHtml import modifyDiffHTML
from AStyleToolModules.RhapsodyFilesAStyleHandler import UnformattedRhapsodyFile
from AStyleToolModules.DiffWindow import DiffWindow
from AStyleToolModules.AStyleGUIAbstractClass import IntegratedAStyleFrame



class MainApplication(IntegratedAStyleFrame):
    def __init__(self, parent, title):
        IntegratedAStyleFrame.__init__(self, parent, title)

        #self.rhapsodyFileFormatIncludeConstructorsCheckBox.Disable() #FDEV: disable features for formatting constructors and destructors
        #self.rhapsodyFileFormatIncludeDestructorsCheckBox.Disable() #FDEV: disable features for formatting constructors and destructors

        self.singleFileFormatShowDiffCheckBox.Disable();

        self.includeOperations = self.rhapsodyFileFormatIncludeOperationsCheckBox.IsChecked()
        self.includeTransitions = self.rhapsodyFileFormatIncludeTransitionsCheckBox.IsChecked()
        self.includeStates = self.rhapsodyFileFormatIncludeStatesCheckBox.IsChecked()
        self.includeDestructors = False #self.rhapsodyFileFormatIncludeDestructorsCheckBox.IsChecked()
        self.includeConstructors = False #self.rhapsodyFileFormatIncludeConstructorsCheckBox.IsChecked()

        self.includeHFiles = self.recursiveFormatIncludeHFilesCheckBox.IsChecked()
        self.includeHppFiles = self.recursiveFormatIncludeHppFilesCheckBox.IsChecked()
        self.includeCppFiles = self.recursiveFormatIncludeCppFilesCheckBox.IsChecked()

        self.showDiff = self.singleFileFormatShowDiffCheckBox.IsChecked()

    def __del__( self ):
        pass

    # Virtual event handlers, overide them in your derived class

    def showModal(self, modalText):
        dlg = wx.MessageDialog( self, modalText, "Notice", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.


    def execAstyle(self, filePathStr):
        astyleOptions = ["--style=ansi", "--indent=spaces=4", "--pad-oper", "--pad-header",
                        "--unpad-paren", "--add-brackets", "--indent-namespaces", "--indent-switches"]

        astyleOptions.append("--suffix=.0r16") #choosen unique extension for original file for easier tracking

        sysCall = ["astyle.exe"] + astyleOptions + [filePathStr]
        proc = subprocess.Popen(sysCall, stdout=subprocess.PIPE)
        stdout, stderr = proc.communicate()
        time.sleep(0.15)

        return stdout


    def OnSingleFileFormatLoadFileButtonClick( self, event ):
        self.singleFileFormatSummaryFileNameLabelValueStaticText.SetLabel("")
        self.singleFileFormatSummaryStatusValueStaticText.SetLabel("")

        dlg = wx.FileDialog(self, wildcard = 'C++ files (.cpp, .hpp, .h) | *.cpp;*.hpp;*.h', style=wx.OPEN)
        if dlg.ShowModal():
            self.singleFileFormatPathStr = dlg.GetPath()
            self.singleFileFormatPathDisplay.SetValue(self.singleFileFormatPathStr)
            self.GUI_StatusBar.SetStatusText('Ready')
        dlg.Destroy()


    def OnSingleFileFormatExecuteButtonClick( self, event ):
        if self.singleFileFormatPathStr:
            res = self.execAstyle(self.singleFileFormatPathStr)
            self.GUI_StatusBar.SetStatusText(res)

            if 'Formatted' in res:
                if self.showDiff:
                    differ = difflib.HtmlDiff()
                    orig = open(self.singleFileFormatPathStr).read()
                    conv = open(self.singleFileFormatPathStr+'.0r16').read()

                    htmlVer = differ.make_file(conv.split('\n'), orig.split('\n'))
                    f = file(self.singleFileFormatPathStr+'.html', 'w')
                    f.write(htmlVer)
                    f.close()

                    modifyDiffHTML(htmlVer, self.singleFileFormatPathStr)

                    frame = DiffWindow(fpath=self.singleFileFormatPathStr, parent=None, id=wx.ID_ANY, title="AStyle Diff Window", size=(1600, 850), style=wx.MAXIMIZE)
                else:
                    self.showModal("File successfully formatted.")
                    self.singleFileFormatSummaryStatusValueStaticText.SetLabel("Successfully formated the given file.")
            else:
                self.showModal("File unchanged. The file is already in correct format.")
                self.singleFileFormatSummaryStatusValueStaticText.SetLabel("No changes made. The file is already in correct format.")

            self.singleFileFormatSummaryFileNameLabelValueStaticText.SetLabel(self.singleFileFormatPathStr.split('\\')[-1])

        else:
            self.showModal("No file has been uploaded.")

        self.singleFileFormatPathDisplay.SetValue("")
        self.singleFileFormatPathStr = ""


    def OnSingleFileFormatShowDIffCheckBoxCheck( self, event ):
        if event.Checked():
            self.showDiff = True
        else:
            self.showDiff = False


    def OnRecursiveFormatLoadDirectoryButtonClick( self, event ):
        dlg = wx.DirDialog(self, style=wx.OPEN)
        if dlg.ShowModal():
            self.recursiveFormatPathStr = dlg.GetPath()
            self.recursiveFormatPathDisplay.SetValue(self.recursiveFormatPathStr)
            self.GUI_StatusBar.SetStatusText('Ready')
        dlg.Destroy()


    def OnRecursiveFormatExecuteButtonClick( self, event ):
        if self.recursiveFormatPathStr:
            leadingPath = '\\'.join(self.recursiveFormatPathStr.split('\\')[:-1])

            userPath = os.environ['USERPROFILE']
            backupPath = userPath + "\\RecursiveAStyleBackupFiles"

            timeOfCreation = time.localtime()[:6]
            backupPath = backupPath + "\\" + "-".join(map(lambda x: str(int(x)), timeOfCreation[3:])) + "_" + "-".join(map(lambda x: str(x), timeOfCreation[:3][::-1]))


            svnFolder = ".svn"

            self.cppFilesList = []
            self.hppFilesList = []
            self.hFilesList = []

            self.numberOfFormattedCppFiles = 0
            self.numberOfFormattedHppFiles = 0
            self.numberOfFormattedHFiles = 0

            walker = os.walk(self.recursiveFormatPathStr)

            for path, dirs, files in walker:
                if svnFolder in dirs:
                    dirs.remove(svnFolder)
                for fileName in files:
                    if (self.includeCppFiles and ("cpp" == fileName.split(".")[-1])):
                        self.cppFilesList.append(os.path.join(path, fileName))
                    elif (self.includeHppFiles and ("hpp" == fileName.split(".")[-1])):
                        self.hppFilesList.append(os.path.join(path, fileName))
                    elif (self.includeHFiles and ("h" == fileName.split(".")[-1])):
                        self.hFilesList.append(os.path.join(path, fileName))

            #Note: Add implementation of progress bar here later
            affectedFiles = len(self.cppFilesList) + len(self.hppFilesList) + len(self.hFilesList)

            if affectedFiles:
                progressMax = 100
                dialog = wx.ProgressDialog("Converting...", "Time remaining", progressMax,
                style=wx.PD_ELAPSED_TIME | wx.PD_REMAINING_TIME) #wx.PD_CAN_ABORT |

                inc = 100.0/affectedFiles
                keepGoing = True
                count = 0

                for cppFile in self.cppFilesList:
                    count += inc
                    keepGoing = dialog.Update(count)
                    res = self.execAstyle(cppFile)
                    if "Formatted" in res:
                        self.numberOfFormattedCppFiles += 1
                        backupFilePath = cppFile.replace(leadingPath, backupPath)

                        if not os.path.exists(os.path.dirname(backupFilePath)):
                            os.makedirs(os.path.dirname(backupFilePath))

                        shutil.move(cppFile + ".0r16", backupFilePath)

                for hppFile in self.hppFilesList:
                    count += inc
                    keepGoing = dialog.Update(count)
                    res = self.execAstyle(hppFile)
                    if "Formatted" in res:
                        self.numberOfFormattedHppFiles += 1
                        backupFilePath = hppFile.replace(leadingPath, backupPath)

                        if not os.path.exists(os.path.dirname(backupFilePath)):
                            os.makedirs(os.path.dirname(backupFilePath))

                        shutil.move(hppFile + ".0r16", backupFilePath)

                for hFile in self.hFilesList:
                    count += inc
                    keepGoing = dialog.Update(count)
                    res = self.execAstyle(hFile)
                    if "Formatted" in res:
                        self.numberOfFormattedHFiles += 1
                        backupFilePath = hFile.replace(leadingPath, backupPath)

                        if not os.path.exists(os.path.dirname(backupFilePath)):
                            os.makedirs(os.path.dirname(backupFilePath))

                        shutil.move(hFile + ".0r16", backupFilePath)

                dialog.Destroy()

                self.GUI_StatusBar.SetStatusText("Original files stored in: %s" % backupPath)
            else:
                self.GUI_StatusBar.SetStatusText("No changes made. Files are in correct format.")

            #Update valued in Summary
            self.summaryCppTotalMetricValue.SetLabel(str(len(self.cppFilesList)))
            self.summaryHppTotalMetricValue.SetLabel(str(len(self.hppFilesList)))
            self.summaryHTotalMetricValue.SetLabel(str(len(self.hFilesList)))

            self.summaryCppFormattedMetricValue.SetLabel(str(self.numberOfFormattedCppFiles))
            self.summaryHppFormattedMetricValue.SetLabel(str(self.numberOfFormattedHppFiles))
            self.summaryHFormattedMetricValue.SetLabel(str(self.numberOfFormattedHFiles))

            self.showModal("Completed recursive application of AStyle to the specified directory!\n\nOriginal files are backed-up in:\n\t    %s" % backupPath)
        else:
            self.showModal("No directory has been specified.")

        self.recursiveFormatPathDisplay.SetValue("")
        self.recursiveFormatPathStr = ""


    def OnRecursiveFormatIncludeCppFilesCheckBoxCheck( self, event ):
        if event.Checked():
            self.includeCppFiles = True
        else:
            self.includeCppFiles = False


    def OnRecursiveFormatIncludeHppFilesCheckBoxCheck( self, event ):
        if event.Checked():
            self.includeHppFiles = True
        else:
            self.includeHppFiles = False


    def OnRecursiveFormatIncludeHFilesCheckBoxCheck( self, event ):
        if event.Checked():
            self.includeHFiles = True
        else:
            self.includeHFiles = False


    def OnRhapsodyFormatLoadFileButtonClick( self, event ):
        self.rhapsodyFileFormatSummaryFileNameLabelValueStaticText.SetLabel("")
        self.rhapsodyFileFormatSummaryStatusValueStaticText.SetLabel("")

        dlg = wx.FileDialog(self, wildcard = 'Rhapsody files (*.cls, *.sbs) | *.cls;*.sbs', style=wx.OPEN)
        if dlg.ShowModal():
            self.rhapsodyFileFormatPathStr = dlg.GetPath()
            self.rhapsodyFileFormatPathDisplay.SetValue(self.rhapsodyFileFormatPathStr)
            self.GUI_StatusBar.SetStatusText('Ready')
        dlg.Destroy()


    def OnRhapsodyFormatExecuteButtonClick( self, event ):
        if self.rhapsodyFileFormatPathStr:
            progressMax = 100
            dialog = wx.ProgressDialog("Converting...", "Time remaining", progressMax,
            style=wx.PD_ELAPSED_TIME | wx.PD_REMAINING_TIME) #wx.PD_CAN_ABORT |

            keepGoing = True
            count = 0

            isRhapsodyFileFormatted = False

            rhapsodyFile = open(self.rhapsodyFileFormatPathStr)
            rhapsodyFileContent = rhapsodyFile.read()
            rhapsodyFile.close()

            UnformattedRhapsodyFileObject = UnformattedRhapsodyFile(rhapsodyFileContent)
            opTypeAndChoicePairs = [('Constructors', self.includeConstructors),
                            ('Destructors', self.includeDestructors),
                            ('States', self.includeStates),
                            ('Transitions', self.includeTransitions),
                            ('Operations', self.includeOperations)]
            inc = 100/len(opTypeAndChoicePairs) # 100% / number of operations

            for opType, decision in opTypeAndChoicePairs:
                count += inc
                keepGoing = dialog.Update(count)

                if ('Constructors' == opType) and decision:
                    isRhapsodyFileFormatted = isRhapsodyFileFormatted or UnformattedRhapsodyFileObject.astyleRhapsodyConstructor()

                if ('Destructors' == opType) and decision:
                    isRhapsodyFileFormatted = isRhapsodyFileFormatted or UnformattedRhapsodyFileObject.astyleRhapsodyDestructor()

                if ('States' == opType) and decision:
                    isRhapsodyFileFormatted = isRhapsodyFileFormatted or UnformattedRhapsodyFileObject.astyleRhapsodyState()

                if ('Transitions' == opType) and decision:
                    isRhapsodyFileFormatted = isRhapsodyFileFormatted or UnformattedRhapsodyFileObject.astyleRhapsodyTransition()
                    isRhapsodyFileFormatted = isRhapsodyFileFormatted or UnformattedRhapsodyFileObject.astyleRhapsodyCGITrans()

                if ('Operations' == opType) and decision:
                    isRhapsodyFileFormatted = isRhapsodyFileFormatted or UnformattedRhapsodyFileObject.astyleRhapsodyPrimitiveOperations()

            keepGoing = dialog.Update(100)
            dialog.Destroy()

            if isRhapsodyFileFormatted:
                shutil.copy(self.rhapsodyFileFormatPathStr, self.rhapsodyFileFormatPathStr + ".unAStyledRhapsodyFile")
                os.chmod(self.rhapsodyFileFormatPathStr, 0777)
                os.remove(self.rhapsodyFileFormatPathStr)
                formattedRhapsodyFile = file(self.rhapsodyFileFormatPathStr, 'w')
                formattedRhapsodyFile.write(UnformattedRhapsodyFileObject.File)

                time.sleep(0.5) #Allow file to complete operation before closing it.
                formattedRhapsodyFile.close()

                self.showModal("Successfully performed AStyle on selected Rhapsody file.")
                self.rhapsodyFileFormatSummaryStatusValueStaticText.SetLabel("Successfully formated the given file.")
            else:
                self.showModal("No need to format chosen Rhapsody file.")
                self.rhapsodyFileFormatSummaryStatusValueStaticText.SetLabel("No changes made. The file is already in correct format.")

            self.rhapsodyFileFormatSummaryFileNameLabelValueStaticText.SetLabel(self.rhapsodyFileFormatPathStr.split('\\')[-1])

        else:
            self.showModal("No Rhapsody file has been loaded.")

        self.rhapsodyFileFormatPathDisplay.SetValue("")
        self.rhapsodyFileFormatPathStr = ""


    def OnRhapsodyFormatIncludeConstructorsCheckBoxCheck( self, event ):
        if event.Checked():
            self.includeConstructors = True
        else:
            self.includeConstructors = False


    def OnRhapsodyFormatIncludeDestructorsCheckBoxCheck( self, event ):
        if event.Checked():
            self.includeDestructors = True
        else:
            self.includeDestructors = False


    def OnRhapsodyFormatIncludeStatesCheckBoxCheck( self, event ):
        if event.Checked():
            self.includeStates = True
        else:
            self.includeStates = False


    def OnRhapsodyFormatIncludeTransitionsCheckBoxCheck( self, event ):
        if event.Checked():
            self.includeTransitions = True
        else:
            self.includeTransitions = False


    def OnRhapsodyFormatIncludeOperationsCheckBoxCheck( self, event ):
        if event.Checked():
            self.includeOperations = True
        else:
            self.includeOperations = False



if __name__=="__main__":
    app = wx.App(False)
    frame = MainApplication(parent=None, title="Original AStyle Manager")
    frame.Show()
    app.MainLoop()
