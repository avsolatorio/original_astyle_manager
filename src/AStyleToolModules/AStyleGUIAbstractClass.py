#-------------------------------------------------------------------------------
# Name:        AStyleGUIAbstractClass.py
# Purpose:
#
# Author:      avsolatorio
#
# Created:     02/06/2014
# Copyright:   (c) avsolatorio 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import wx
import wx.xrc

###########################################################################
## Class IntegratedAStyleFrame
###########################################################################

class IntegratedAStyleFrame ( wx.Frame ):

    def __init__( self, parent, title ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = title, pos = wx.DefaultPosition, size = wx.Size( 650,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        self.SetSizeHintsSz( wx.Size( 650,400 ), wx.Size( 650,400 ) )

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

        self.singleFileFormatPathDisplay = wx.TextCtrl( self.notebookSingleFileOption, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        singleFileFormatLoadButtonSizer.Add( self.singleFileFormatPathDisplay, 1, wx.ALL, 5 )


        singleFileFormatFileSelectionStaticBoxSizer.Add( singleFileFormatLoadButtonSizer, 1, wx.EXPAND, 5 )

        singleFileFormatExecuteButtonSizer = wx.BoxSizer( wx.HORIZONTAL )


        singleFileFormatExecuteButtonSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

        self.singleFileFormatExecuteButton = wx.Button( self.notebookSingleFileOption, wx.ID_ANY, u"AStyle It!", wx.DefaultPosition, wx.DefaultSize, 0 )
        singleFileFormatExecuteButtonSizer.Add( self.singleFileFormatExecuteButton, 0, wx.ALL, 5 )


        singleFileFormatFileSelectionStaticBoxSizer.Add( singleFileFormatExecuteButtonSizer, 1, wx.EXPAND, 5 )


        singleFileFormatLeftSizer.Add( singleFileFormatFileSelectionStaticBoxSizer, 1, wx.EXPAND, 5 )

        singleFileFormatSummaryStaticBoxSizer = wx.StaticBoxSizer( wx.StaticBox( self.notebookSingleFileOption, wx.ID_ANY, u"Summary" ), wx.VERTICAL )

        singleFileFormatSummaryUpperBoxSizer = wx.BoxSizer( wx.VERTICAL )

        self.singleFileFormatSummaryTextTitle = wx.StaticText( self.notebookSingleFileOption, wx.ID_ANY, u"File formatting status.", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.singleFileFormatSummaryTextTitle.Wrap( -1 )
        singleFileFormatSummaryUpperBoxSizer.Add( self.singleFileFormatSummaryTextTitle, 0, wx.ALL, 5 )


        singleFileFormatSummaryStaticBoxSizer.Add( singleFileFormatSummaryUpperBoxSizer, 0, wx.EXPAND, 5 )

        singleFileFormatSummaryLowerBoxSizer = wx.BoxSizer( wx.HORIZONTAL )

        singleFileFormatSummaryLowerLeftBoxSizer = wx.BoxSizer( wx.VERTICAL )

        self.singleFileFormatSummaryFileNameLabelStaticText = wx.StaticText( self.notebookSingleFileOption, wx.ID_ANY, u"    File name:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.singleFileFormatSummaryFileNameLabelStaticText.Wrap( -1 )
        singleFileFormatSummaryLowerLeftBoxSizer.Add( self.singleFileFormatSummaryFileNameLabelStaticText, 0, wx.ALL, 5 )

        self.singleFileFormatSummaryStatusStaticText = wx.StaticText( self.notebookSingleFileOption, wx.ID_ANY, u"    Status:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.singleFileFormatSummaryStatusStaticText.Wrap( -1 )
        singleFileFormatSummaryLowerLeftBoxSizer.Add( self.singleFileFormatSummaryStatusStaticText, 0, wx.ALL, 5 )


        singleFileFormatSummaryLowerBoxSizer.Add( singleFileFormatSummaryLowerLeftBoxSizer, 0, wx.EXPAND, 5 )

        singleFileFormatSummaryLowerRightBoxSizer = wx.BoxSizer( wx.VERTICAL )

        self.singleFileFormatSummaryFileNameLabelValueStaticText = wx.StaticText( self.notebookSingleFileOption, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.singleFileFormatSummaryFileNameLabelValueStaticText.Wrap( -1 )
        singleFileFormatSummaryLowerRightBoxSizer.Add( self.singleFileFormatSummaryFileNameLabelValueStaticText, 0, wx.ALL, 5 )

        self.singleFileFormatSummaryStatusValueStaticText = wx.StaticText( self.notebookSingleFileOption, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.singleFileFormatSummaryStatusValueStaticText.Wrap( -1 )
        singleFileFormatSummaryLowerRightBoxSizer.Add( self.singleFileFormatSummaryStatusValueStaticText, 0, wx.ALL, 5 )


        singleFileFormatSummaryLowerBoxSizer.Add( singleFileFormatSummaryLowerRightBoxSizer, 1, wx.EXPAND, 5 )


        singleFileFormatSummaryStaticBoxSizer.Add( singleFileFormatSummaryLowerBoxSizer, 1, wx.EXPAND, 5 )


        singleFileFormatLeftSizer.Add( singleFileFormatSummaryStaticBoxSizer, 1, wx.EXPAND, 5 )


        singleFormatSizer.Add( singleFileFormatLeftSizer, 10, wx.EXPAND, 5 )

        singleFileFormatRightStaticBoxSizer = wx.StaticBoxSizer( wx.StaticBox( self.notebookSingleFileOption, wx.ID_ANY, u"Post Formatting Options:" ), wx.VERTICAL )

        self.singleFileFormatShowDiffCheckBox = wx.CheckBox( self.notebookSingleFileOption, wx.ID_ANY, u"Show diff", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.singleFileFormatShowDiffCheckBox.SetValue(False)
        singleFileFormatRightStaticBoxSizer.Add( self.singleFileFormatShowDiffCheckBox, 0, wx.ALL, 5 )


        singleFormatSizer.Add( singleFileFormatRightStaticBoxSizer, 3, wx.EXPAND, 5 )


        self.notebookSingleFileOption.SetSizer( singleFormatSizer )
        self.notebookSingleFileOption.Layout()
        singleFormatSizer.Fit( self.notebookSingleFileOption )
        self.globalNotebook.AddPage( self.notebookSingleFileOption, u"Single File Format", True )
        self.notebookRecursiveFormatOption = wx.Panel( self.globalNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        recursiveFormatSizer = wx.BoxSizer( wx.HORIZONTAL )

        recursiveFormatLeftSizer = wx.BoxSizer( wx.VERTICAL )

        recursiveFormatFileSelectionStaticBoxSizer = wx.StaticBoxSizer( wx.StaticBox( self.notebookRecursiveFormatOption, wx.ID_ANY, u"Directory Selection" ), wx.VERTICAL )

        recursiveFormatLoadButtonSizer = wx.BoxSizer( wx.HORIZONTAL )

        self.recursiveFormatLoadButton = wx.Button( self.notebookRecursiveFormatOption, wx.ID_ANY, u"Load Directory", wx.DefaultPosition, wx.DefaultSize, 0 )
        recursiveFormatLoadButtonSizer.Add( self.recursiveFormatLoadButton, 0, wx.ALL, 5 )

        self.recursiveFormatPathDisplay = wx.TextCtrl( self.notebookRecursiveFormatOption, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        recursiveFormatLoadButtonSizer.Add( self.recursiveFormatPathDisplay, 1, wx.ALL, 5 )


        recursiveFormatFileSelectionStaticBoxSizer.Add( recursiveFormatLoadButtonSizer, 1, wx.EXPAND, 5 )

        recursiveFormatExecuteButtonSizer = wx.BoxSizer( wx.HORIZONTAL )


        recursiveFormatExecuteButtonSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

        self.recursiveFormatExecuteButton = wx.Button( self.notebookRecursiveFormatOption, wx.ID_ANY, u"AStyle It!", wx.DefaultPosition, wx.DefaultSize, 0 )
        recursiveFormatExecuteButtonSizer.Add( self.recursiveFormatExecuteButton, 0, wx.ALL, 5 )


        recursiveFormatFileSelectionStaticBoxSizer.Add( recursiveFormatExecuteButtonSizer, 1, wx.EXPAND, 5 )


        recursiveFormatLeftSizer.Add( recursiveFormatFileSelectionStaticBoxSizer, 1, wx.EXPAND, 5 )

        recursiveFormatSummaryStaticBoxSizer = wx.StaticBoxSizer( wx.StaticBox( self.notebookRecursiveFormatOption, wx.ID_ANY, u"Summary" ), wx.HORIZONTAL )

        recursiveFormatSummaryMetricsColumnBoxSizer = wx.BoxSizer( wx.VERTICAL )

        self.summaryMetricsHeader = wx.StaticText( self.notebookRecursiveFormatOption, wx.ID_ANY, u"Metrics", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.summaryMetricsHeader.Wrap( -1 )
        recursiveFormatSummaryMetricsColumnBoxSizer.Add( self.summaryMetricsHeader, 0, wx.ALL, 5 )

        self.summaryTotalMetric = wx.StaticText( self.notebookRecursiveFormatOption, wx.ID_ANY, u"Total Files Found          ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.summaryTotalMetric.Wrap( -1 )
        recursiveFormatSummaryMetricsColumnBoxSizer.Add( self.summaryTotalMetric, 0, wx.ALL, 5 )

        self.summaryFormattedMetric = wx.StaticText( self.notebookRecursiveFormatOption, wx.ID_ANY, u"Formatted Files          ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.summaryFormattedMetric.Wrap( -1 )
        recursiveFormatSummaryMetricsColumnBoxSizer.Add( self.summaryFormattedMetric, 0, wx.ALL, 5 )


        recursiveFormatSummaryStaticBoxSizer.Add( recursiveFormatSummaryMetricsColumnBoxSizer, 0, wx.EXPAND, 5 )

        recursiveFormatSummaryCppColumnBoxSizer = wx.BoxSizer( wx.VERTICAL )

        self.summaryCppHeader = wx.StaticText( self.notebookRecursiveFormatOption, wx.ID_ANY, u"*.cpp Files", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.summaryCppHeader.Wrap( -1 )
        recursiveFormatSummaryCppColumnBoxSizer.Add( self.summaryCppHeader, 0, wx.ALL, 5 )

        self.summaryCppTotalMetricValue = wx.StaticText( self.notebookRecursiveFormatOption, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.summaryCppTotalMetricValue.Wrap( -1 )
        recursiveFormatSummaryCppColumnBoxSizer.Add( self.summaryCppTotalMetricValue, 0, wx.ALL, 5 )

        self.summaryCppFormattedMetricValue = wx.StaticText( self.notebookRecursiveFormatOption, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.summaryCppFormattedMetricValue.Wrap( -1 )
        recursiveFormatSummaryCppColumnBoxSizer.Add( self.summaryCppFormattedMetricValue, 0, wx.ALL, 5 )


        recursiveFormatSummaryStaticBoxSizer.Add( recursiveFormatSummaryCppColumnBoxSizer, 1, wx.EXPAND, 5 )

        recursiveFormatSummaryHppColumnBoxSizer = wx.BoxSizer( wx.VERTICAL )

        self.summaryHppHeader = wx.StaticText( self.notebookRecursiveFormatOption, wx.ID_ANY, u"*.hpp Files", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.summaryHppHeader.Wrap( -1 )
        recursiveFormatSummaryHppColumnBoxSizer.Add( self.summaryHppHeader, 0, wx.ALL, 5 )

        self.summaryHppTotalMetricValue = wx.StaticText( self.notebookRecursiveFormatOption, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.summaryHppTotalMetricValue.Wrap( -1 )
        recursiveFormatSummaryHppColumnBoxSizer.Add( self.summaryHppTotalMetricValue, 0, wx.ALL, 5 )

        self.summaryHppFormattedMetricValue = wx.StaticText( self.notebookRecursiveFormatOption, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.summaryHppFormattedMetricValue.Wrap( -1 )
        recursiveFormatSummaryHppColumnBoxSizer.Add( self.summaryHppFormattedMetricValue, 0, wx.ALL, 5 )


        recursiveFormatSummaryStaticBoxSizer.Add( recursiveFormatSummaryHppColumnBoxSizer, 1, wx.EXPAND, 5 )

        recursiveFormatSummaryHColumnBoxSizer = wx.BoxSizer( wx.VERTICAL )

        self.summaryHHeader = wx.StaticText( self.notebookRecursiveFormatOption, wx.ID_ANY, u"*.h Files", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.summaryHHeader.Wrap( -1 )
        recursiveFormatSummaryHColumnBoxSizer.Add( self.summaryHHeader, 0, wx.ALL, 5 )

        self.summaryHTotalMetricValue = wx.StaticText( self.notebookRecursiveFormatOption, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.summaryHTotalMetricValue.Wrap( -1 )
        recursiveFormatSummaryHColumnBoxSizer.Add( self.summaryHTotalMetricValue, 0, wx.ALL, 5 )

        self.summaryHFormattedMetricValue = wx.StaticText( self.notebookRecursiveFormatOption, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.summaryHFormattedMetricValue.Wrap( -1 )
        recursiveFormatSummaryHColumnBoxSizer.Add( self.summaryHFormattedMetricValue, 0, wx.ALL, 5 )


        recursiveFormatSummaryStaticBoxSizer.Add( recursiveFormatSummaryHColumnBoxSizer, 1, wx.EXPAND, 5 )


        recursiveFormatLeftSizer.Add( recursiveFormatSummaryStaticBoxSizer, 1, wx.EXPAND, 5 )


        recursiveFormatSizer.Add( recursiveFormatLeftSizer, 4, wx.EXPAND, 5 )

        recursiveFormatRightStaticBoxSizer = wx.StaticBoxSizer( wx.StaticBox( self.notebookRecursiveFormatOption, wx.ID_ANY, u"File Types to Format:" ), wx.VERTICAL )

        self.recursiveFormatIncludeCppFilesCheckBox = wx.CheckBox( self.notebookRecursiveFormatOption, wx.ID_ANY, u"*.cpp", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.recursiveFormatIncludeCppFilesCheckBox.SetValue(True)
        recursiveFormatRightStaticBoxSizer.Add( self.recursiveFormatIncludeCppFilesCheckBox, 0, wx.ALL, 5 )

        self.recursiveFormatIncludeHppFilesCheckBox = wx.CheckBox( self.notebookRecursiveFormatOption, wx.ID_ANY, u"*.hpp", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.recursiveFormatIncludeHppFilesCheckBox.SetValue(True)
        recursiveFormatRightStaticBoxSizer.Add( self.recursiveFormatIncludeHppFilesCheckBox, 0, wx.ALL, 5 )

        self.recursiveFormatIncludeHFilesCheckBox = wx.CheckBox( self.notebookRecursiveFormatOption, wx.ID_ANY, u"*.h", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.recursiveFormatIncludeHFilesCheckBox.SetValue(True)
        recursiveFormatRightStaticBoxSizer.Add( self.recursiveFormatIncludeHFilesCheckBox, 0, wx.ALL, 5 )


        recursiveFormatSizer.Add( recursiveFormatRightStaticBoxSizer, 1, wx.EXPAND, 5 )


        self.notebookRecursiveFormatOption.SetSizer( recursiveFormatSizer )
        self.notebookRecursiveFormatOption.Layout()
        recursiveFormatSizer.Fit( self.notebookRecursiveFormatOption )
        self.globalNotebook.AddPage( self.notebookRecursiveFormatOption, u"Recursive Format", False )
        self.notebookRhapsodyFormatOption = wx.Panel( self.globalNotebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        rhapsodyFileFormatSizer = wx.BoxSizer( wx.HORIZONTAL )

        rhrhapsodyFileFormatLeftSizer = wx.BoxSizer( wx.VERTICAL )

        rhapsodyFileFormatFileSelectionStaticBoxSizer = wx.StaticBoxSizer( wx.StaticBox( self.notebookRhapsodyFormatOption, wx.ID_ANY, u"File Selection" ), wx.VERTICAL )

        rhapsodyFileFormatLoadButtonSizer = wx.BoxSizer( wx.HORIZONTAL )

        self.rhapsodrhapsodyFileFormatLoadButton = wx.Button( self.notebookRhapsodyFormatOption, wx.ID_ANY, u"Load File", wx.DefaultPosition, wx.DefaultSize, 0 )
        rhapsodyFileFormatLoadButtonSizer.Add( self.rhapsodrhapsodyFileFormatLoadButton, 0, wx.ALL, 5 )

        self.rhapsodyFileFormatPathDisplay = wx.TextCtrl( self.notebookRhapsodyFormatOption, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
        rhapsodyFileFormatLoadButtonSizer.Add( self.rhapsodyFileFormatPathDisplay, 1, wx.ALL, 5 )


        rhapsodyFileFormatFileSelectionStaticBoxSizer.Add( rhapsodyFileFormatLoadButtonSizer, 1, wx.EXPAND, 10 )

        rhapsodyFileFormatExecuteButtonSizer = wx.BoxSizer( wx.HORIZONTAL )


        rhapsodyFileFormatExecuteButtonSizer.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

        self.rhapsodyFileFormatExecuteButton = wx.Button( self.notebookRhapsodyFormatOption, wx.ID_ANY, u"AStyle It!", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
        rhapsodyFileFormatExecuteButtonSizer.Add( self.rhapsodyFileFormatExecuteButton, 0, wx.ALL, 5 )


        rhapsodyFileFormatFileSelectionStaticBoxSizer.Add( rhapsodyFileFormatExecuteButtonSizer, 1, wx.EXPAND, 5 )


        rhrhapsodyFileFormatLeftSizer.Add( rhapsodyFileFormatFileSelectionStaticBoxSizer, 1, wx.EXPAND, 5 )

        rhapsodyFileFormatSummaryStaticBoxSizer = wx.StaticBoxSizer( wx.StaticBox( self.notebookRhapsodyFormatOption, wx.ID_ANY, u"Summary" ), wx.VERTICAL )

        rhapsodyFileFormatSummaryUpperBoxSizer = wx.BoxSizer( wx.VERTICAL )

        self.rhapsodyFileFormatSummaryTextTitle = wx.StaticText( self.notebookRhapsodyFormatOption, wx.ID_ANY, u"File formatting status.", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.rhapsodyFileFormatSummaryTextTitle.Wrap( -1 )
        rhapsodyFileFormatSummaryUpperBoxSizer.Add( self.rhapsodyFileFormatSummaryTextTitle, 0, wx.ALL, 5 )


        rhapsodyFileFormatSummaryStaticBoxSizer.Add( rhapsodyFileFormatSummaryUpperBoxSizer, 0, wx.EXPAND, 5 )

        rhapsodyFileFormatSummaryLowerBoxSizer = wx.BoxSizer( wx.HORIZONTAL )

        rhapsodyFileFormatSummaryLowerLeftBoxSizer = wx.BoxSizer( wx.VERTICAL )

        self.rhapsodyFileFormatSummaryFileNameLabelStaticText = wx.StaticText( self.notebookRhapsodyFormatOption, wx.ID_ANY, u"    File name:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.rhapsodyFileFormatSummaryFileNameLabelStaticText.Wrap( -1 )
        rhapsodyFileFormatSummaryLowerLeftBoxSizer.Add( self.rhapsodyFileFormatSummaryFileNameLabelStaticText, 0, wx.ALL, 5 )

        self.rhapsodyFileFormatSummaryStatusStaticText = wx.StaticText( self.notebookRhapsodyFormatOption, wx.ID_ANY, u"    Status:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.rhapsodyFileFormatSummaryStatusStaticText.Wrap( -1 )
        rhapsodyFileFormatSummaryLowerLeftBoxSizer.Add( self.rhapsodyFileFormatSummaryStatusStaticText, 0, wx.ALL, 5 )


        rhapsodyFileFormatSummaryLowerBoxSizer.Add( rhapsodyFileFormatSummaryLowerLeftBoxSizer, 0, wx.EXPAND, 5 )

        rhapsodyFileFormatSummaryLowerRightBoxSizer = wx.BoxSizer( wx.VERTICAL )

        self.rhapsodyFileFormatSummaryFileNameLabelValueStaticText = wx.StaticText( self.notebookRhapsodyFormatOption, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.rhapsodyFileFormatSummaryFileNameLabelValueStaticText.Wrap( -1 )
        rhapsodyFileFormatSummaryLowerRightBoxSizer.Add( self.rhapsodyFileFormatSummaryFileNameLabelValueStaticText, 0, wx.ALL, 5 )

        self.rhapsodyFileFormatSummaryStatusValueStaticText = wx.StaticText( self.notebookRhapsodyFormatOption, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.rhapsodyFileFormatSummaryStatusValueStaticText.Wrap( -1 )
        rhapsodyFileFormatSummaryLowerRightBoxSizer.Add( self.rhapsodyFileFormatSummaryStatusValueStaticText, 0, wx.ALL, 5 )


        rhapsodyFileFormatSummaryLowerBoxSizer.Add( rhapsodyFileFormatSummaryLowerRightBoxSizer, 1, wx.EXPAND, 5 )


        rhapsodyFileFormatSummaryStaticBoxSizer.Add( rhapsodyFileFormatSummaryLowerBoxSizer, 1, wx.EXPAND, 5 )


        rhrhapsodyFileFormatLeftSizer.Add( rhapsodyFileFormatSummaryStaticBoxSizer, 1, wx.EXPAND, 5 )


        rhapsodyFileFormatSizer.Add( rhrhapsodyFileFormatLeftSizer, 1, wx.EXPAND, 5 )

        rhapsodyFileFormatRightStaticBoxSizer = wx.StaticBoxSizer( wx.StaticBox( self.notebookRhapsodyFormatOption, wx.ID_ANY, u"Apply AStyle to:" ), wx.VERTICAL )

        self.rhapsodyFileFormatIncludeConstructorsCheckBox = wx.CheckBox( self.notebookRhapsodyFormatOption, wx.ID_ANY, u"Constructors     ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.rhapsodyFileFormatIncludeConstructorsCheckBox.Enable( False )

        rhapsodyFileFormatRightStaticBoxSizer.Add( self.rhapsodyFileFormatIncludeConstructorsCheckBox, 0, wx.ALL, 5 )

        self.rhapsodyFileFormatIncludeDestructorsCheckBox = wx.CheckBox( self.notebookRhapsodyFormatOption, wx.ID_ANY, u"Destructors", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.rhapsodyFileFormatIncludeDestructorsCheckBox.Enable( False )

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
        self.globalNotebook.AddPage( self.notebookRhapsodyFormatOption, u"Rhapsody File Format", False )

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


        globalSizer.Add( subGlobalLowerSizer, 1, wx.EXPAND, 0 )


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
        self.recursiveFormatLoadButton.Bind( wx.EVT_BUTTON, self.OnRecursiveFormatLoadDirectoryButtonClick )
        self.recursiveFormatExecuteButton.Bind( wx.EVT_BUTTON, self.OnRecursiveFormatExecuteButtonClick )
        self.recursiveFormatIncludeCppFilesCheckBox.Bind( wx.EVT_CHECKBOX, self.OnRecursiveFormatIncludeCppFilesCheckBoxCheck )
        self.recursiveFormatIncludeHppFilesCheckBox.Bind( wx.EVT_CHECKBOX, self.OnRecursiveFormatIncludeHppFilesCheckBoxCheck )
        self.recursiveFormatIncludeHFilesCheckBox.Bind( wx.EVT_CHECKBOX, self.OnRecursiveFormatIncludeHFilesCheckBoxCheck )
        self.rhapsodrhapsodyFileFormatLoadButton.Bind( wx.EVT_BUTTON, self.OnRhapsodyFormatLoadFileButtonClick )
        self.rhapsodyFileFormatExecuteButton.Bind( wx.EVT_BUTTON, self.OnRhapsodyFormatExecuteButtonClick )
        self.rhapsodyFileFormatIncludeConstructorsCheckBox.Bind( wx.EVT_CHECKBOX, self.OnRhapsodyFormatIncludeConstructorsCheckBoxCheck )
        self.rhapsodyFileFormatIncludeDestructorsCheckBox.Bind( wx.EVT_CHECKBOX, self.OnRhapsodyFormatIncludeDestructorsCheckBoxCheck )
        self.rhapsodyFileFormatIncludeStatesCheckBox.Bind( wx.EVT_CHECKBOX, self.OnRhapsodyFormatIncludeStatesCheckBoxCheck )
        self.rhapsodyFileFormatIncludeTransitionsCheckBox.Bind( wx.EVT_CHECKBOX, self.OnRhapsodyFormatIncludeTransitionsCheckBoxCheck )
        self.rhapsodyFileFormatIncludeOperationsCheckBox.Bind( wx.EVT_CHECKBOX, self.OnRhapsodyFormatIncludeOperationsCheckBoxCheck )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def OnSingleFileFormatLoadFileButtonClick( self, event ):
        event.Skip()

    def OnSingleFileFormatExecuteButtonClick( self, event ):
        event.Skip()

    def OnSingleFileFormatShowDIffCheckBoxCheck( self, event ):
        event.Skip()

    def OnRecursiveFormatLoadDirectoryButtonClick( self, event ):
        event.Skip()

    def OnRecursiveFormatExecuteButtonClick( self, event ):
        event.Skip()

    def OnRecursiveFormatIncludeCppFilesCheckBoxCheck( self, event ):
        event.Skip()

    def OnRecursiveFormatIncludeHppFilesCheckBoxCheck( self, event ):
        event.Skip()

    def OnRecursiveFormatIncludeHFilesCheckBoxCheck( self, event ):
        event.Skip()

    def OnRhapsodyFormatLoadFileButtonClick( self, event ):
        event.Skip()

    def OnRhapsodyFormatExecuteButtonClick( self, event ):
        event.Skip()

    def OnRhapsodyFormatIncludeConstructorsCheckBoxCheck( self, event ):
        event.Skip()

    def OnRhapsodyFormatIncludeDestructorsCheckBoxCheck( self, event ):
        event.Skip()

    def OnRhapsodyFormatIncludeStatesCheckBoxCheck( self, event ):
        event.Skip()

    def OnRhapsodyFormatIncludeTransitionsCheckBoxCheck( self, event ):
        event.Skip()

    def OnRhapsodyFormatIncludeOperationsCheckBoxCheck( self, event ):
        event.Skip()


#if __name__=="__main__":
#    app = wx.App(False)
#    frame = IntegratedAStyleFrame(parent=None, title="Integrated AStyle Tool")
#    frame.Show()
#    app.MainLoop()
