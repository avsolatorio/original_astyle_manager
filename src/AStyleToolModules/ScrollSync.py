#-------------------------------------------------------------------------------
# Name:        ScrollSync.py
# Purpose:
#
# Author:      avsolatorio
#
# Created:     20/05/2014
# Copyright:   (c) avsolatorio 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import wx

def main():
    pass

class ScrollSync(wx.EvtHandler):
    def __init__(self, frame1, frame2):
        super(ScrollSync, self).__init__()
        self.frame1 = frame1
        self.frame2 = frame2
        self.frame1ScrollPos = self.getFrame1Pos()
        self.frame2ScrollPos = self.getFrame2Pos()
        self.Bind(wx.EVT_TIMER, self.onTimer)
        self.timer = wx.Timer(self)
        self.timer.Start(20)

    def onTimer(self, event):
        if not self.frame1 or not self.frame2:
            self.timer.Stop()
            return
        if self.frame1ScrollPos != self.getFrame1Pos():
            self.frame1ScrollPos = self.getFrame1Pos()
            self.frame2.Scroll(self.frame1ScrollPos)
        elif self.frame2ScrollPos != self.getFrame2Pos():
            self.frame2ScrollPos = self.getFrame2Pos()
            self.frame1.Scroll(self.frame2ScrollPos)

    def getFrame1Pos(self):
        horizontal = self.frame1.GetScrollPos(wx.SB_HORIZONTAL)
        vertical = self.frame1.GetScrollPos(wx.SB_VERTICAL)
        return horizontal, vertical

    def getFrame2Pos(self):
        horizontal = self.frame2.GetScrollPos(wx.SB_HORIZONTAL)
        vertical = self.frame2.GetScrollPos(wx.SB_VERTICAL)
        return horizontal, vertical


if __name__ == '__main__':
    main()
