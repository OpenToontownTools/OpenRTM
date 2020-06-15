from direct.showbase import ShowBase
from panda3d.core import loadPrcFile
import builtins
import importlib
from pandac.PandaModules import *
loadPrcFile("Configrc.prc")

class RTMBase(ShowBase.ShowBase):
    def __init__(self):
        ShowBase.ShowBase.__init__(self)
        
        self.startDirect(1, 1, 0)
        from toontown.toon import RobotToonManager
        base.rtm = RobotToonManager.RobotToonManager()
        base.rtm.popupControls()
        camera.setPosHpr(0,-60,5,0,0,0)
        
    def startDirect(self, fWantDirect = 1, fWantTk = 1, fWantWx = 0):
        self.startTk(fWantTk)
        self.startWx(fWantWx)
        self.wantDirect = fWantDirect
        if self.wantDirect:
            # Use importlib to prevent this import from being picked up
            # by modulefinder when packaging an application.
            DirectSession = importlib.import_module('directtools.DirectSession')
            self.direct = DirectSession.DirectSession()
            self.direct.enable()
            builtins.direct = self.direct
        else:
            builtins.direct = self.direct = None

        
base = RTMBase
RTMBase().run()