#-------------------------------------------------------------------------------
# Name:        RhapsodyFilesAStyleHandler.py
# Purpose:
#
# Author:      avsolatorio
#
# Created:     20/05/2014
# Copyright:   (c) avsolatorio 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import time
import subprocess
import re
import os

def main():
    pass

class UnformattedRhapsodyFile( object ):
    def __init__(self, fileContent):
        self.File = fileContent
        self.tempFileName = "tempFile.temp"
        self.delimeter = "\n--end--\n"
        self.current_method = '__init__'

    def set_current_method(self, methodName):
        self.current_method = methodName

    def execAstyle(self):
        astyleOptions = ["--style=ansi", "--indent=spaces=4", "--pad-oper", "--pad-header",
                    "--unpad-paren", "--add-brackets", "--indent-namespaces", "--indent-switches"]

        proc = subprocess.Popen(["astyle.exe"] + astyleOptions + [self.tempFileName], stdout=subprocess.PIPE)
        stdout, stderr = proc.communicate()
        time.sleep(1)
        print stdout
        return stdout

    def execChange(self, originalSnippet, astyledSnippet):
        #p = re.compile(originalSnippet)
        #return p.sub(astyledSnippet, originalFile)
        listFormatFile = list(self.File)
        listFormatAStyledSnippet = list(astyledSnippet)

        assert(originalSnippet in self.File)

        sizeOfOriginalSnippet = len(originalSnippet)
        originalPos = self.File.find(originalSnippet)
        self.File = ''.join(listFormatFile[:originalPos] + listFormatAStyledSnippet + listFormatFile[originalPos + sizeOfOriginalSnippet:])

    def getBody(self, origBody, tempFile, IPrimitiveOperation=False):
        if IPrimitiveOperation:
            temp = '"'.join(origBody.split("_bodyData")[-1].split('"')[1:-1])
        else:
            temp = '"'.join(origBody.split('"')[1:-1])

        if temp.count("\n") > 0:
            temp = temp.replace('\\"', '"')
            tempFile.write(temp.strip('\n'))
            tempFile.write(self.delimeter)
            return temp.replace('"', '\\"')
        else:
            return None

    def cleanList(self, listToClean):
        '''Remove None types in originalSnippets list if self.getBody returns None'''
        try:
            while True:
                listToClean.remove(None)
        except:
            pass

    def performModifications(self, originalSnippets):
        returnValue = False
        if 'Formatted' in self.execAstyle():
            tempFile = open(self.tempFileName)

            for snippet, j in zip(originalSnippets, tempFile.read().strip(self.delimeter).split(self.delimeter)):
                newJ = j.replace('"', '\\"')
                self.execChange(snippet, newJ)

            tempFile.close()
            returnValue = True #returns True which means that AStyle was used

        os.remove(self.tempFileName)
        return returnValue

    def astyleRhapsodyConstructors(self):
        returnValue = False
        return returnValue
    #    self.set_current_method('astyleRhapsodyConstructors')

    #   tempFile = file(self.tempFileName, 'w')
    #    MatchConstructor = re.search('IConstructor \n[\w\W]*?_constant =[\w\W]*?_itsBody = \{ IBody [\w\W]*?_bodyData = "[\w\W]*?";\n\t{3}\}\n\t{2}\}\n\t\}?', self.File)

    #    if MatchConstructor:
    #        originalSnippets = []
    #        for i in MatchConstructor.re.findall(self.File):
    #            originalSnippets.append(self.getBody(i, tempFile, IPrimitiveOperation=True))

    #        self.cleanList(originalSnippets)
    #        tempFile.close()

    #        self.performModifications(originalSnippets)

    def astyleRhapsodyDestructors(self):
        returnValue = False
        return returnValue
    #    self.set_current_method('astyleRhapsodyDestructors')

    #    tempFile = file(self.tempFileName, 'w')
    #    MatchDestructor = re.search('IDestructor \n[\w\W]*?_constant =[\w\W]*?_itsBody = \{ IBody [\w\W]*?_bodyData = "[\w\W]*?";\n\t{3}\}\n\t{2}\}\n\t\}?', self.File)

    #    if MatchDestructor:
    #        originalSnippets = []
    #        for i in MatchDestructor.re.findall(self.File):
    #            originalSnippets.append(self.getBody(i, tempFile, IPrimitiveOperation=True))

    #        self.cleanList(originalSnippets)
    #        tempFile.close()

    #        self.performModifications(originalSnippets)

    def astyleRhapsodyPrimitiveOperations(self):
        returnValue = False
        self.set_current_method('astyleRhapsodyPrimitiveOperations')

        tempFile = file(self.tempFileName, 'w')
        MatchPrimitiveOperation = re.search('IPrimitiveOperation \n[\w\W]*?_constant =[\w\W]*?_itsBody = \{ IBody [\w\W]*?_bodyData = "[\w\W]*?";\n\t{3}\}\n\t{2}\}\n\t\}?', self.File)

        if MatchPrimitiveOperation:
            originalSnippets = []
            for i in MatchPrimitiveOperation.re.findall(self.File):
                originalSnippets.append(self.getBody(i, tempFile, IPrimitiveOperation=True))

            self.cleanList(originalSnippets)
            tempFile.close()

            returnValue = self.performModifications(originalSnippets)

        return returnValue

    def astyleRhapsodyTransition(self):
        returnValue = False
        self.set_current_method('astyleRhapsodyTransition')

        tempFile = file(self.tempFileName, 'w')
        MatchTransitionAction = re.search('_itsAction = \{ IAction [\w\W]*?_id = [\w\W]*?_body = "[\w\W]*?";\n[\w\W]*?_itsTarget', self.File)

        if MatchTransitionAction:
            originalSnippets = []
            for i in MatchTransitionAction.re.findall(self.File):
                originalSnippets.append(self.getBody(i, tempFile))

            self.cleanList(originalSnippets)
            tempFile.close()

            returnValue = self.performModifications(originalSnippets)

        return returnValue

    def astyleRhapsodyState(self):
        returnValue = False
        self.set_current_method('astyleRhapsodyState')

        tempFile = file(self.tempFileName, 'w')
        MatchStateAction = re.search('_entryAction = { IAction [\w\W]*?_id = [\w\W]*?_myState = [\w\W]*?_body = "[\w\W]*?";\n\t{5,}\}', self.File)

        if MatchStateAction:
            originalSnippets = []
            for i in MatchStateAction.re.findall(self.File):
                originalSnippets.append(self.getBody(i, tempFile))

            self.cleanList(originalSnippets)
            tempFile.close()

            returnValue = self.performModifications(originalSnippets)

        return returnValue

    def astyleRhapsodyCGITrans(self):
        returnValue = False
        self.set_current_method('astyleRhapsodyCGITrans')

        tempFile = file(self.tempFileName, 'w')
        MatchCGITrans = re.search('m_rpn = { CGIText \n[\w\W]*?m_str = [\w\W]*?m_style', self.File)

        if MatchCGITrans:
            originalSnippets = []
            for i in MatchCGITrans.re.findall(self.File):
                originalSnippets.append(self.getBody(i, tempFile))

            self.cleanList(originalSnippets)
            tempFile.close()

            returnValue = self.performModifications(originalSnippets)

        return returnValue

    def astyleRhapsodyFile(self):
        self.astyleRhapsodyTransition()
        self.astyleRhapsodyState()
        self.astyleRhapsodyCGITrans()
        self.astyleRhapsodyPrimitiveOperations()

if __name__ == '__main__':
    main()
