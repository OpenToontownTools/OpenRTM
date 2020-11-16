''' Open Robot Toon Manager Base Class '''
from direct.showbase import ShowBase
from panda3d.core import loadPrcFile
import builtins
import importlib
from pandac.PandaModules import *

class RTMBase(ShowBase.ShowBase):
    def __init__(self):
        # Load the prc file prior to launching showbase in order
        # to have it affect window related stuff
        loadPrcFile("Configrc.prc")
        
        ShowBase.ShowBase.__init__(self)

        # Import the main dlls so we don't have to repeatedly import them everywhere
        builtins.__dict__.update(__import__('panda3d.core', fromlist=['*']).__dict__)
        builtins.__dict__.update(__import__('libotp', fromlist=['*']).__dict__)
        builtins.__dict__.update(__import__('libtoontown', fromlist=['*']).__dict__)

        self.startDirect(1, 1, 0)
        from toontown.toon import RobotToonManager
        base.rtm = RobotToonManager.RobotToonManager()
        base.rtm.popupControls()
        camera.setPosHpr(0, -60, 5, 0, 0, 0)

base = RTMBase
RTMBase().run()
