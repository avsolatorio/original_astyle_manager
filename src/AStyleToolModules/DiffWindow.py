#-------------------------------------------------------------------------------
# Name:        DiffWindow.py
# Purpose:
#
# Author:      avsolatorio
#
# Created:     28/05/2014
# Copyright:   (c) avsolatorio89 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import wx
from ScrollSync import ScrollSync

def main():
    pass

class DiffWindow(wx.Frame):
    def __init__(self, **kwargs):
        wx.Frame.__init__(self, id=kwargs['id'], parent=kwargs['parent'], title=kwargs['title'], size=kwargs['size'], style=wx.DEFAULT_FRAME_STYLE ^ wx.MAXIMIZE)

        self.fname = kwargs['fpath']

        self.origFilePath = self.fname[:self.fname.rindex('.')]+'_orig.html'
        self.convFilePath = self.fname[:self.fname.rindex('.')]+'_conv.html'

        self.htmlWinOrig = wx.html.HtmlWindow(self, wx.ID_ANY)
        self.splitterLine = wx.Panel(self)
        self.htmlWinConv = wx.html.HtmlWindow(self, wx.ID_ANY)

        self.htmlWinOrig.LoadPage(self.origFilePath)
        self.htmlWinConv.LoadPage(self.convFilePath)

        self.CreateStatusBar() # A StatusBar in the bottom of the window

        # Setting up the menu.
        filemenu= wx.Menu()
        helpmenu= wx.Menu()

        # wx.ID_ABOUT and wx.ID_EXIT are standard ids provided by wxWidgets.
        menuAbout = helpmenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
        menuBar.Append(helpmenu,"&Help") # Adding the "helpmenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

        # Set events.
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_CLOSE, self.OnExit)

        self.sizerOrig = wx.BoxSizer(wx.VERTICAL)
        self.origLabel = wx.TextCtrl(self, id=wx.ID_ANY, style=wx.TE_READONLY|wx.TE_CENTER)
        self.origLabel.SetValue('Original File')
        self.origLabel.SetBackgroundColour((128,128,255))
        self.sizerOrig.Add(self.origLabel, 0.5, wx.ALL|wx.EXPAND)
        self.sizerOrig.Add(self.htmlWinOrig, 20, wx.ALL|wx.EXPAND)

        self.sizerConv = wx.BoxSizer(wx.VERTICAL)
        self.convLabel = wx.TextCtrl(self, id=wx.ID_ANY, style=wx.TE_READONLY|wx.TE_CENTER)
        self.convLabel.SetValue('AStyled File')
        self.convLabel.SetBackgroundColour((128,128,255))
        self.sizerConv.Add(self.convLabel, 0.5, wx.ALL|wx.EXPAND)
        self.sizerConv.Add(self.htmlWinConv, 20, wx.ALL|wx.EXPAND)

        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.sizerOrig, 20, wx.ALL|wx.EXPAND)
        self.sizer.Add(self.splitterLine, 0.1, wx.ALL)
        self.sizer.Add(self.sizerConv, 20, wx.ALL|wx.EXPAND)
        self.SetSizer(self.sizer)

        self.Layout()
        ScrollSync(self.htmlWinOrig, self.htmlWinConv)
        self.Show()

    def OnAbout(self,e):
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
        dlg = wx.MessageDialog( self, "Diff of original and AStyled codes.", "About AStyle Diff Window", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.

    def OnExit(self,e):
        try:
            os.remove(self.origFilePath)
        except:
            pass
        try:
            os.remove(self.convFilePath)
        except:
            pass
        try:
            os.remove(self.fname+".html")
        except:
            pass
        self.Destroy()


if __name__ == '__main__':
    main()
