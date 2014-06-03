# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Feb 26 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class IntegratedAStyleFrame
###########################################################################

import wx.html
import difflib
import shutil
import re
import os
import subprocess
import sys
import time
from AStyleToolModules.AStyleDiffHtml import modifyDiffHTML
from AStyleToolModules.RhapsodyFilesAStyleHandler import UnformattedRhapsodyFile
from AStyleToolModules.DiffWindow import DiffWindow

#http://jaist.dl.sourceforge.net/project/wxpython/wxPython/3.0.0.0/wxPython3.0-win64-3.0.0.0-py27.exe


class IntegratedAStyleFrame ( wx.Frame ):

    def __init__( self, parent, title ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = title, pos = wx.DefaultPosition, size = wx.Size( 650,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        globalSizer = wx.BoxSizer( wx.VERTICAL )

        subGlobalUpperSizer = wx.BoxSizer( wx.VERTICAL )

        taskStaticBoxSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Choose Type of Task" ), wx.VERTICAL )

        self.globalNotebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.notebookSingleFileOption = wx.Panel( self.globalNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        singleFormatSizer = wx.BoxSizer( wx.HORIZONTAL )

        singleFileFormatLeftSizer = wx.BoxSizer( wx.VERTICAL )

        singleFileFormatFileSelectionStaticBoxSizer = wx.StaticBoxSizer( wx.StaticBox( self.notebookSingleFileOption, wx.ID_ANY, u"File Selection" ), wx.VERTICAL )

        singleFileFormatLoadButtonSizer = wx.BoxSizer( wx.HORIZONTAL )

        self.singleFileFomatLoadButton = wx.Button( self.notebookSingleFileOption, wx.ID_ANY, u"Load File", wx.DefaultPosition, wx.DefaultSize, 0 )
        singleFileFormatLoadButtonSizer.Add( self.singleFileFomatLoadButton, 0, wx.ALL, 5 )

        self.singleFileFormatPathDisplay = wx.TextCtrl( self.notebookSingleFileOption, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        singleFileFormatLoadButtonSizer.Add( self.singleFileFormatPathDisplay, 1, wx.ALL, 5 )


        singleFileFormatFileSelectionStaticBoxSizer.Add( singleFileFormatLoadButtonSizer, 1, wx.EXPAND, 5 )

        singleFileFormatExecuteButtonSizer = wx.BoxSizer( wx.HORIZONTAL )


        singleFileFormatExecuteButtonSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

        self.singleFileFormatExecuteButton = wx.Button( self.notebookSingleFileOption, wx.ID_ANY, u"AStyle It!", wx.DefaultPosition, wx.DefaultSize, 0 )
        singleFileFormatExecuteButtonSizer.Add( self.singleFileFormatExecuteButton, 0, wx.ALL, 5 )


        singleFileFormatFileSelectionStaticBoxSizer.Add( singleFileFormatExecuteButtonSizer, 1, wx.EXPAND, 5 )


        singleFileFormatLeftSizer.Add( singleFileFormatFileSelectionStaticBoxSizer, 1, wx.EXPAND, 5 )

        singleFileFormatSummaryStaticBoxSizer = wx.StaticBoxSizer( wx.StaticBox( self.notebookSingleFileOption, wx.ID_ANY, u"Summary" ), wx.VERTICAL )


        singleFileFormatLeftSizer.Add( singleFileFormatSummaryStaticBoxSizer, 1, wx.EXPAND, 5 )


        singleFormatSizer.Add( singleFileFormatLeftSizer, 3, wx.EXPAND, 5 )

        singleFileFormatRightStaticBoxSizer = wx.StaticBoxSizer( wx.StaticBox( self.notebookSingleFileOption, wx.ID_ANY, u"Post Formatting Options" ), wx.VERTICAL )

        self.singleFileFormatShowDiffCheckBox = wx.CheckBox( self.notebookSingleFileOption, wx.ID_ANY, u"Show diff", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.singleFileFormatShowDiffCheckBox.SetValue(True)
        singleFileFormatRightStaticBoxSizer.Add( self.singleFileFormatShowDiffCheckBox, 0, wx.ALL, 5 )

        self.singleFileFormatRemoveOriginalFileCheckBox = wx.CheckBox( self.notebookSingleFileOption, wx.ID_ANY, u"Remove original file", wx.DefaultPosition, wx.DefaultSize, 0 )
        singleFileFormatRightStaticBoxSizer.Add( self.singleFileFormatRemoveOriginalFileCheckBox, 0, wx.ALL, 5 )


        singleFormatSizer.Add( singleFileFormatRightStaticBoxSizer, 0, wx.EXPAND, 5 )


        self.notebookSingleFileOption.SetSizer( singleFormatSizer )
        self.notebookSingleFileOption.Layout()
        singleFormatSizer.Fit( self.notebookSingleFileOption )
        self.globalNotebook.AddPage( self.notebookSingleFileOption, u"Single File Format", False )
        self.notebookRecursiveFormatOption = wx.Panel( self.globalNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        recursiveFormatSizer = wx.BoxSizer( wx.HORIZONTAL )

        recursiveFormatLeftSizer = wx.BoxSizer( wx.VERTICAL )

        recursiveFormatFileSelectionStaticBoxSizer = wx.StaticBoxSizer( wx.StaticBox( self.notebookRecursiveFormatOption, wx.ID_ANY, u"Directory Selection" ), wx.VERTICAL )

        recursiveFormatLoadButtonSizer = wx.BoxSizer( wx.HORIZONTAL )

        self.recursiveFormatLoadButton = wx.Button( self.notebookRecursiveFormatOption, wx.ID_ANY, u"Load Directory", wx.DefaultPosition, wx.DefaultSize, 0 )
        recursiveFormatLoadButtonSizer.Add( self.recursiveFormatLoadButton, 0, wx.ALL, 5 )

        self.recursiveFormatPathDisplay = wx.TextCtrl( self.notebookRecursiveFormatOption, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        recursiveFormatLoadButtonSizer.Add( self.recursiveFormatPathDisplay, 1, wx.ALL, 5 )


        recursiveFormatFileSelectionStaticBoxSizer.Add( recursiveFormatLoadButtonSizer, 1, wx.EXPAND, 5 )

        recursiveFormatExecuteButtonSizer = wx.BoxSizer( wx.HORIZONTAL )


        recursiveFormatExecuteButtonSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

        self.recursiveFormatExecuteButton = wx.Button( self.notebookRecursiveFormatOption, wx.ID_ANY, u"AStyle It!", wx.DefaultPosition, wx.DefaultSize, 0 )
        recursiveFormatExecuteButtonSizer.Add( self.recursiveFormatExecuteButton, 0, wx.ALL, 5 )


        recursiveFormatFileSelectionStaticBoxSizer.Add( recursiveFormatExecuteButtonSizer, 1, wx.EXPAND, 5 )


        recursiveFormatLeftSizer.Add( recursiveFormatFileSelectionStaticBoxSizer, 1, wx.EXPAND, 5 )

        recursiveFormatSummaryStaticBoxSizer = wx.StaticBoxSizer( wx.StaticBox( self.notebookRecursiveFormatOption, wx.ID_ANY, u"Summary" ), wx.VERTICAL )

        gSizer2 = wx.GridSizer( 3, 4, 0, 0 )

        self.summaryMetricsHeader = wx.StaticText( self.notebookRecursiveFormatOption, wx.ID_ANY, u"Metrics", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.summaryMetricsHeader.Wrap( -1 )
        gSizer2.Add( self.summaryMetricsHeader, 0, wx.ALL, 5 )

        self.summaryCppHeader = wx.StaticText( self.notebookRecursiveFormatOption, wx.ID_ANY, u"*.cpp Files", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.summaryCppHeader.Wrap( -1 )
        gSizer2.Add( self.summaryCppHeader, 0, wx.ALL, 5 )

        self.summaryHppHeader = wx.StaticText( self.notebookRecursiveFormatOption, wx.ID_ANY, u"*.hpp Files", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.summaryHppHeader.Wrap( -1 )
        gSizer2.Add( self.summaryHppHeader, 0, wx.ALL, 5 )

        self.summaryHHeader = wx.StaticText( self.notebookRecursiveFormatOption, wx.ID_ANY, u"*.h Files", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.summaryHHeader.Wrap( -1 )
        gSizer2.Add( self.summaryHHeader, 0, wx.ALL, 5 )

        self.summaryTotalMetric = wx.StaticText( self.notebookRecursiveFormatOption, wx.ID_ANY, u"Total Files Found", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.summaryTotalMetric.Wrap( -1 )
        gSizer2.Add( self.summaryTotalMetric, 0, wx.ALL, 5 )

        self.summaryCppTotalMetricValue = wx.StaticText( self.notebookRecursiveFormatOption, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.summaryCppTotalMetricValue.Wrap( -1 )
        gSizer2.Add( self.summaryCppTotalMetricValue, 0, wx.ALL, 5 )

        self.summaryHppTotalMetricValue = wx.StaticText( self.notebookRecursiveFormatOption, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.summaryHppTotalMetricValue.Wrap( -1 )
        gSizer2.Add( self.summaryHppTotalMetricValue, 0, wx.ALL, 5 )

        self.summaryHTotalMetricValue = wx.StaticText( self.notebookRecursiveFormatOption, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.summaryHTotalMetricValue.Wrap( -1 )
        gSizer2.Add( self.summaryHTotalMetricValue, 0, wx.ALL, 5 )

        self.summaryFormattedMetric = wx.StaticText( self.notebookRecursiveFormatOption, wx.ID_ANY, u"Formatted Files", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.summaryFormattedMetric.Wrap( -1 )
        gSizer2.Add( self.summaryFormattedMetric, 0, wx.ALL, 5 )

        self.summaryCppFormattedMetricValue = wx.StaticText( self.notebookRecursiveFormatOption, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.summaryCppFormattedMetricValue.Wrap( -1 )
        gSizer2.Add( self.summaryCppFormattedMetricValue, 0, wx.ALL, 5 )

        self.summaryHppFormattedMetricValue = wx.StaticText( self.notebookRecursiveFormatOption, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.summaryHppFormattedMetricValue.Wrap( -1 )
        gSizer2.Add( self.summaryHppFormattedMetricValue, 0, wx.ALL, 5 )

        self.summaryHFormattedMetricValue = wx.StaticText( self.notebookRecursiveFormatOption, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.summaryHFormattedMetricValue.Wrap( -1 )
        gSizer2.Add( self.summaryHFormattedMetricValue, 0, wx.ALL, 5 )


        recursiveFormatSummaryStaticBoxSizer.Add( gSizer2, 1, wx.EXPAND, 5 )


        recursiveFormatLeftSizer.Add( recursiveFormatSummaryStaticBoxSizer, 1, wx.EXPAND, 5 )


        recursiveFormatSizer.Add( recursiveFormatLeftSizer, 1, wx.EXPAND, 5 )

        recursiveFormatRightStaticBoxSizer = wx.StaticBoxSizer( wx.StaticBox( self.notebookRecursiveFormatOption, wx.ID_ANY, u"File Types to Format" ), wx.VERTICAL )

        self.recursiveFormatIncludeCppFilesCheckBox = wx.CheckBox( self.notebookRecursiveFormatOption, wx.ID_ANY, u"*.cpp", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.recursiveFormatIncludeCppFilesCheckBox.SetValue(True)
        recursiveFormatRightStaticBoxSizer.Add( self.recursiveFormatIncludeCppFilesCheckBox, 0, wx.ALL, 5 )

        self.recursiveFormatIncludeHppFilesCheckBox = wx.CheckBox( self.notebookRecursiveFormatOption, wx.ID_ANY, u"*.hpp", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.recursiveFormatIncludeHppFilesCheckBox.SetValue(True)
        recursiveFormatRightStaticBoxSizer.Add( self.recursiveFormatIncludeHppFilesCheckBox, 0, wx.ALL, 5 )

        self.recursiveFormatIncludeHFilesCheckBox = wx.CheckBox( self.notebookRecursiveFormatOption, wx.ID_ANY, u"*.h", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.recursiveFormatIncludeHFilesCheckBox.SetValue(True)
        recursiveFormatRightStaticBoxSizer.Add( self.recursiveFormatIncludeHFilesCheckBox, 0, wx.ALL, 5 )


        recursiveFormatSizer.Add( recursiveFormatRightStaticBoxSizer, 0, wx.EXPAND, 5 )


        self.notebookRecursiveFormatOption.SetSizer( recursiveFormatSizer )
        self.notebookRecursiveFormatOption.Layout()
        recursiveFormatSizer.Fit( self.notebookRecursiveFormatOption )
        self.globalNotebook.AddPage( self.notebookRecursiveFormatOption, u"Recursive Format", False )
        self.notebookRhapsodyFormatOption = wx.Panel( self.globalNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        rhapsodyFileFormatSizer = wx.BoxSizer( wx.HORIZONTAL )

        rhapsodyFileFormatLeftSizer = wx.BoxSizer( wx.VERTICAL )

        rhapsodyFileFormatFileSelectionStaticBoxSizer = wx.StaticBoxSizer( wx.StaticBox( self.notebookRhapsodyFormatOption, wx.ID_ANY, u"File Selection" ), wx.VERTICAL )

        rhapsodyFileFormatLoadButtonSizer = wx.BoxSizer( wx.HORIZONTAL )

        self.rhapsodyFileFormatLoadButton = wx.Button( self.notebookRhapsodyFormatOption, wx.ID_ANY, u"Load File", wx.DefaultPosition, wx.DefaultSize, 0 )
        rhapsodyFileFormatLoadButtonSizer.Add( self.rhapsodyFileFormatLoadButton, 0, wx.ALL, 5 )

        self.rhapsodyFileFormatPathDisplay = wx.TextCtrl( self.notebookRhapsodyFormatOption, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        rhapsodyFileFormatLoadButtonSizer.Add( self.rhapsodyFileFormatPathDisplay, 1, wx.ALL, 5 )


        rhapsodyFileFormatFileSelectionStaticBoxSizer.Add( rhapsodyFileFormatLoadButtonSizer, 1, wx.EXPAND, 10 )

        rhapsodyFileFormatExecuteButtonSizer = wx.BoxSizer( wx.HORIZONTAL )


        rhapsodyFileFormatExecuteButtonSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

        self.rhapsodyFileFormatExecuteButton = wx.Button( self.notebookRhapsodyFormatOption, wx.ID_ANY, u"AStyle It!", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
        rhapsodyFileFormatExecuteButtonSizer.Add( self.rhapsodyFileFormatExecuteButton, 0, wx.ALL, 5 )


        rhapsodyFileFormatFileSelectionStaticBoxSizer.Add( rhapsodyFileFormatExecuteButtonSizer, 1, wx.EXPAND, 5 )


        rhapsodyFileFormatLeftSizer.Add( rhapsodyFileFormatFileSelectionStaticBoxSizer, 1, wx.EXPAND, 5 )

        rhapsodyFileFormatSummaryStaticBoxSizer = wx.StaticBoxSizer( wx.StaticBox( self.notebookRhapsodyFormatOption, wx.ID_ANY, u"Summary" ), wx.VERTICAL )


        rhapsodyFileFormatLeftSizer.Add( rhapsodyFileFormatSummaryStaticBoxSizer, 1, wx.EXPAND, 5 )


        rhapsodyFileFormatSizer.Add( rhapsodyFileFormatLeftSizer, 1, wx.EXPAND, 5 )

        rhapsodyFileFormatRightStaticBoxSizer = wx.StaticBoxSizer( wx.StaticBox( self.notebookRhapsodyFormatOption, wx.ID_ANY, u"Apply AStyle to:" ), wx.VERTICAL )

        self.rhapsodyFileFormatIncludeConstructorsCheckBox = wx.CheckBox( self.notebookRhapsodyFormatOption, wx.ID_ANY, u"Constructors     ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.rhapsodyFileFormatIncludeConstructorsCheckBox.SetValue(True)
        rhapsodyFileFormatRightStaticBoxSizer.Add( self.rhapsodyFileFormatIncludeConstructorsCheckBox, 0, wx.ALL, 5 )

        self.rhapsodyFileFormatIncludeDestructorsCheckBox = wx.CheckBox( self.notebookRhapsodyFormatOption, wx.ID_ANY, u"Destructors", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.rhapsodyFileFormatIncludeDestructorsCheckBox.SetValue(True)
        rhapsodyFileFormatRightStaticBoxSizer.Add( self.rhapsodyFileFormatIncludeDestructorsCheckBox, 0, wx.ALL, 5 )

        self.rhapsodyFileFormatIncludeStatesCheckBox = wx.CheckBox( self.notebookRhapsodyFormatOption, wx.ID_ANY, u"States", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.rhapsodyFileFormatIncludeStatesCheckBox.SetValue(True)
        rhapsodyFileFormatRightStaticBoxSizer.Add( self.rhapsodyFileFormatIncludeStatesCheckBox, 0, wx.ALL, 5 )

        self.rhapsodyFileFormatIncludeTransitionsCheckBox = wx.CheckBox( self.notebookRhapsodyFormatOption, wx.ID_ANY, u"Transitions", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.rhapsodyFileFormatIncludeTransitionsCheckBox.SetValue(True)
        rhapsodyFileFormatRightStaticBoxSizer.Add( self.rhapsodyFileFormatIncludeTransitionsCheckBox, 0, wx.ALL, 5 )

        self.rhapsodyFileFormatIncludeOperationsCheckBox = wx.CheckBox( self.notebookRhapsodyFormatOption, wx.ID_ANY, u"Operations", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.rhapsodyFileFormatIncludeOperationsCheckBox.SetValue(True)
        rhapsodyFileFormatRightStaticBoxSizer.Add( self.rhapsodyFileFormatIncludeOperationsCheckBox, 0, wx.ALL, 5 )


        rhapsodyFileFormatSizer.Add( rhapsodyFileFormatRightStaticBoxSizer, 0, wx.EXPAND, 0 )


        self.notebookRhapsodyFormatOption.SetSizer( rhapsodyFileFormatSizer )
        self.notebookRhapsodyFormatOption.Layout()
        rhapsodyFileFormatSizer.Fit( self.notebookRhapsodyFormatOption )
        self.globalNotebook.AddPage( self.notebookRhapsodyFormatOption, u"Rhapsody File Format", True )
        self.notebookCleanUpAStyleArtefacts = wx.Panel( self.globalNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.globalNotebook.AddPage( self.notebookCleanUpAStyleArtefacts, u"Remove AStyle Artefacts", False )

        taskStaticBoxSizer.Add( self.globalNotebook, 1, wx.EXPAND |wx.ALL, 0 )


        subGlobalUpperSizer.Add( taskStaticBoxSizer, 1, wx.EXPAND, 5 )


        globalSizer.Add( subGlobalUpperSizer, 4, wx.EXPAND, 0 )

        subGlobalLowerSizer = wx.BoxSizer( wx.VERTICAL )

        optionsStaticBoxSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"OAM AStyle Options" ), wx.VERTICAL )

        gridSizer = wx.GridSizer( 1, 4, 0, 0 )

        self.options_set1 = wx.StaticText( self, wx.ID_ANY, u"--style=ansi\n--indent=spaces=4", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.options_set1.Wrap( -1 )
        gridSizer.Add( self.options_set1, 0, wx.ALL, 5 )

        self.options_set2 = wx.StaticText( self, wx.ID_ANY, u"--pad-oper\n--pad-header", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.options_set2.Wrap( -1 )
        gridSizer.Add( self.options_set2, 0, wx.ALL, 5 )

        self.options_set3 = wx.StaticText( self, wx.ID_ANY, u"--unpad-paren\n--add-brackets", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.options_set3.Wrap( -1 )
        gridSizer.Add( self.options_set3, 0, wx.ALL, 5 )

        self.options_set4 = wx.StaticText( self, wx.ID_ANY, u"--indent-namespaces\n--indent-switches", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.options_set4.Wrap( -1 )
        gridSizer.Add( self.options_set4, 0, wx.ALL, 5 )


        optionsStaticBoxSizer.Add( gridSizer, 1, wx.EXPAND, 5 )


        subGlobalLowerSizer.Add( optionsStaticBoxSizer, 1, wx.EXPAND, 5 )


        globalSizer.Add( subGlobalLowerSizer, 2, wx.EXPAND, 0 )


        self.SetSizer( globalSizer )
        self.Layout()
        self.GUI_StatusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
        self.GUI_MenuBar = wx.MenuBar( 0 )
        self.fileMenu = wx.Menu()
        self.GUI_MenuBar.Append( self.fileMenu, u"File" )

        self.helpMenu = wx.Menu()
        self.GUI_MenuBar.Append( self.helpMenu, u"Help" )

        self.SetMenuBar( self.GUI_MenuBar )


        self.Centre( wx.BOTH )

        # Connect Events
        self.singleFileFomatLoadButton.Bind( wx.EVT_BUTTON, self.OnSingleFileFormatLoadFileButtonClick )
        self.singleFileFormatExecuteButton.Bind( wx.EVT_BUTTON, self.OnSingleFileFormatExecuteButtonClick )
        self.singleFileFormatShowDiffCheckBox.Bind( wx.EVT_CHECKBOX, self.OnSingleFileFormatShowDIffCheckBoxCheck )
        self.singleFileFormatRemoveOriginalFileCheckBox.Bind( wx.EVT_CHECKBOX, self.OnSingleFileFormatRemoveOriginalFileCheckBoxCheck )
        self.recursiveFormatLoadButton.Bind( wx.EVT_BUTTON, self.OnRecursiveFormatLoadDirectoryButtonClick )
        self.recursiveFormatExecuteButton.Bind( wx.EVT_BUTTON, self.OnRecursiveFormatExecuteButtonClick )
        self.recursiveFormatIncludeCppFilesCheckBox.Bind( wx.EVT_CHECKBOX, self.OnRecursiveFormatIncludeCppFilesCheckBoxCheck )
        self.recursiveFormatIncludeHppFilesCheckBox.Bind( wx.EVT_CHECKBOX, self.OnRecursiveFormatIncludeHppFilesCheckBoxCheck )
        self.recursiveFormatIncludeHFilesCheckBox.Bind( wx.EVT_CHECKBOX, self.OnRecursiveFormatIncludeHFilesCheckBoxCheck )
        self.rhapsodyFileFormatLoadButton.Bind( wx.EVT_BUTTON, self.OnRhapsodyFormatLoadFileButtonClick )
        self.rhapsodyFileFormatExecuteButton.Bind( wx.EVT_BUTTON, self.OnRhapsodyFormatExecuteButtonClick )
        self.rhapsodyFileFormatIncludeConstructorsCheckBox.Bind( wx.EVT_CHECKBOX, self.OnRhapsodyFormatIncludeConstructorsCheckBoxCheck )
        self.rhapsodyFileFormatIncludeDestructorsCheckBox.Bind( wx.EVT_CHECKBOX, self.OnRhapsodyFormatIncludeDestructorsCheckBoxCheck )
        self.rhapsodyFileFormatIncludeStatesCheckBox.Bind( wx.EVT_CHECKBOX, self.OnRhapsodyFormatIncludeStatesCheckBoxCheck )
        self.rhapsodyFileFormatIncludeTransitionsCheckBox.Bind( wx.EVT_CHECKBOX, self.OnRhapsodyFormatIncludeTransitionsCheckBoxCheck )
        self.rhapsodyFileFormatIncludeOperationsCheckBox.Bind( wx.EVT_CHECKBOX, self.OnRhapsodyFormatIncludeOperationsCheckBoxCheck )


        self.rhapsodyFileFormatIncludeConstructorsCheckBox.Disable() #FDEV: disable features for formatting constructors and destructors
        self.rhapsodyFileFormatIncludeDestructorsCheckBox.Disable() #FDEV: disable features for formatting constructors and destructors

        self.includeOperations = self.rhapsodyFileFormatIncludeOperationsCheckBox.IsChecked()
        self.includeTransitions = self.rhapsodyFileFormatIncludeTransitionsCheckBox.IsChecked()
        self.includeStates = self.rhapsodyFileFormatIncludeStatesCheckBox.IsChecked()
        self.includeDestructors = False #self.rhapsodyFileFormatIncludeDestructorsCheckBox.IsChecked()
        self.includeConstructors = False #self.rhapsodyFileFormatIncludeConstructorsCheckBox.IsChecked()
        self.includeHFiles = self.recursiveFormatIncludeHFilesCheckBox.IsChecked()
        self.includeHppFiles = self.recursiveFormatIncludeHppFilesCheckBox.IsChecked()
        self.includeCppFiles = self.recursiveFormatIncludeCppFilesCheckBox.IsChecked()
        self.removeOriginalFile = self.singleFileFormatRemoveOriginalFileCheckBox.IsChecked()
        self.showDiff = self.singleFileFormatShowDiffCheckBox.IsChecked()
    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class

    def showModal(modalText):
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
        time.sleep(0.2)

        return stdout

    def OnSingleFileFormatLoadFileButtonClick( self, event ):
        dlg = wx.FileDialog(self, wildcard = '*.*', style=wx.OPEN)
        if dlg.ShowModal():
            self.singleFileFormatPathStr = dlg.GetPath()
            self.singleFileFormatPathDisplay.SetValue(self.singleFileFormatPathStr)
            self.GUI_StatusBar.SetStatusText('Ready')
        dlg.Destroy()
        event.Skip()

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
                    showModal("File successfully formatted.")
            else:
                showModal("File unchanged. The file is already in correct format.")
        else:
            showModal("No file has been uploaded.")


    def OnSingleFileFormatShowDIffCheckBoxCheck( self, event ):
        if event.Checked():
            self.showDiff = True
        else:
            self.showDiff = False
        event.Skip()

    def OnSingleFileFormatRemoveOriginalFileCheckBoxCheck( self, event ):
        if event.Checked():
            self.removeOriginalFile = True
        else:
            self.removeOriginalFile = False
        event.Skip()

    def OnRecursiveFormatLoadDirectoryButtonClick( self, event ):
        dlg = wx.DirDialog(self, style=wx.OPEN)
        if dlg.ShowModal():
            self.recursiveFormatPathStr = dlg.GetPath()
            self.recursiveFormatPathDisplay.SetValue(self.recursiveFormatPathStr)
            self.GUI_StatusBar.SetStatusText('Ready')
        dlg.Destroy()
        event.Skip()

    def OnRecursiveFormatExecuteButtonClick( self, event ):
        if self.recursiveFormatPathStr:
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

                for hppFile in self.hppFilesList:
                    count += inc
                    keepGoing = dialog.Update(count)
                    res = self.execAstyle(hppFile)
                    if "Formatted" in res:
                        self.numberOfFormattedHppFiles += 1

                for hFile in self.hFilesList:
                    count += inc
                    keepGoing = dialog.Update(count)
                    res = self.execAstyle(hFile)
                    if "Formatted" in res:
                        self.numberOfFormattedHFiles += 1

            dialog.Destroy()

            self.GUI_StatusBar.SetStatusText("Recursive application of AStyle to root directory %s completed!" % self.recursiveFormatPathStr)

            #Update valued in Summary
            self.summaryCppTotalMetricValue.SetLabel(str(len(self.cppFilesList)))
            self.summaryHppTotalMetricValue.SetLabel(str(len(self.hppFilesList)))
            self.summaryHTotalMetricValue.SetLabel(str(len(self.hFilesList)))

            self.summaryCppFormattedMetricValue.SetLabel(str(self.numberOfFormattedCppFiles))
            self.summaryHppFormattedMetricValue.SetLabel(str(self.numberOfFormattedHppFiles))
            self.summaryHFormattedMetricValue.SetLabel(str(self.numberOfFormattedHFiles))

            dlg = wx.MessageDialog( self, "Completed recursive application of AStyle to the specified directory!", "Notice", wx.OK)
            dlg.ShowModal() # Show it
            dlg.Destroy() # finally destroy it when finished.

        else:
            dlg = wx.MessageDialog( self, "No directory has been specified.", "Notice", wx.OK)
            dlg.ShowModal() # Show it
            dlg.Destroy() # finally destroy it when finished.
        event.Skip()

    def OnRecursiveFormatIncludeCppFilesCheckBoxCheck( self, event ):
        if event.Checked():
            self.includeCppFiles = True
        else:
            self.includeCppFiles = False
        event.Skip()

    def OnRecursiveFormatIncludeHppFilesCheckBoxCheck( self, event ):
        if event.Checked():
            self.includeHppFiles = True
        else:
            self.includeHppFiles = False
        event.Skip()

    def OnRecursiveFormatIncludeHFilesCheckBoxCheck( self, event ):
        if event.Checked():
            self.includeHFiles = True
        else:
            self.includeHFiles = False
        event.Skip()

    def OnRhapsodyFormatLoadFileButtonClick( self, event ):
        dlg = wx.FileDialog(self, wildcard = 'Rhapsody files (*.cls, *.sbs) | *.cls;*.sbs', style=wx.OPEN)
        if dlg.ShowModal():
            self.rhapsodyFileFormatPathStr = dlg.GetPath()
            self.rhapsodyFileFormatPathDisplay.SetValue(self.rhapsodyFileFormatPathStr)
            self.GUI_StatusBar.SetStatusText('Ready')
        dlg.Destroy()
        event.Skip()

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
                    UnformattedRhapsodyFileObject.astyleRhapsodyConstructor()
                    isRhapsodyFileFormatted = True

                if ('Destructors' == opType) and decision:
                    UnformattedRhapsodyFileObject.astyleRhapsodyDestructor()
                    isRhapsodyFileFormatted = True

                if ('States' == opType) and decision:
                    UnformattedRhapsodyFileObject.astyleRhapsodyState()
                    isRhapsodyFileFormatted = True

                if ('Transitions' == opType) and decision:
                    UnformattedRhapsodyFileObject.astyleRhapsodyTransition()
                    UnformattedRhapsodyFileObject.astyleRhapsodyCGITrans()
                    isRhapsodyFileFormatted = True

                if ('Operations' == opType) and decision:
                    UnformattedRhapsodyFileObject.astyleRhapsodyPrimitiveOperations()
                    isRhapsodyFileFormatted = True

            dialog.Destroy()

            if isRhapsodyFileFormatted:
                shutil.copy(self.rhapsodyFileFormatPathStr, self.rhapsodyFileFormatPathStr + ".unAStyledRhapsodyFile")
                os.remove(self.rhapsodyFileFormatPathStr)
                formattedRhapsodyFile = file(self.rhapsodyFileFormatPathStr, 'w')
                formattedRhapsodyFile.write(UnformattedRhapsodyFileObject.File)

                time.sleep(0.5) #Allow file to complete operation before closing it.
                formattedRhapsodyFile.close()

                dlg = wx.MessageDialog( self, "Successfully performed AStyle on selected Rhapsody file.", "Notice", wx.OK)
                dlg.ShowModal() # Show it
                dlg.Destroy() # finally destroy it when finished.
            else:
                dlg = wx.MessageDialog( self, "No need to format chosen Rhapsody file.", "Notice", wx.OK)
                dlg.ShowModal() # Show it
                dlg.Destroy() # finally destroy it when finished.
        else:
            dlg = wx.MessageDialog( self, "No Rhapsody file has been loaded.", "Notice", wx.OK)
            dlg.ShowModal() # Show it
            dlg.Destroy() # finally destroy it when finished.

        event.Skip()

    def OnRhapsodyFormatIncludeConstructorsCheckBoxCheck( self, event ):
        if event.Checked():
            self.includeConstructors = True
        else:
            self.includeConstructors = False
        event.Skip()

    def OnRhapsodyFormatIncludeDestructorsCheckBoxCheck( self, event ):
        if event.Checked():
            self.includeDestructors = True
        else:
            self.includeDestructors = False
        event.Skip()

    def OnRhapsodyFormatIncludeStatesCheckBoxCheck( self, event ):
        if event.Checked():
            self.includeStates = True
        else:
            self.includeStates = False
        event.Skip()

    def OnRhapsodyFormatIncludeTransitionsCheckBoxCheck( self, event ):
        if event.Checked():
            self.includeTransitions = True
        else:
            self.includeTransitions = False
        event.Skip()

    def OnRhapsodyFormatIncludeOperationsCheckBoxCheck( self, event ):
        if event.Checked():
            self.includeOperations = True
        else:
            self.includeOperations = False
        event.Skip()

if __name__=="__main__":
    app = wx.App(False)
    frame = IntegratedAStyleFrame(parent=None, title="Integrated AStyle Tool")
    frame.Show()
    app.MainLoop()