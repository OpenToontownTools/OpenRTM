''' Open Robot Toon Manager Base Class '''
from direct.showbase import ShowBase
from panda3d.core import loadPrcFile
import argparse
import builtins
import importlib
import os
import pathlib
from panda3d.core import *
# move this stuff to a globals
TOONTOWN_ONLINE = 0
TOONTOWN_REWRITTEN = 1
TOONTOWN_CORPORATE_CLASH = 2
TOONTOWN_OFFLINE = 3
SERVER_TO_ID = {'online':    TOONTOWN_ONLINE,
                'rewritten': TOONTOWN_REWRITTEN,
                'clash':     TOONTOWN_CORPORATE_CLASH,
                'offline':   TOONTOWN_OFFLINE
                }

DEFAULT_SERVER = TOONTOWN_ONLINE

class RTMBase(ShowBase.ShowBase):
    def __init__(self):
        # Load the prc file prior to launching showbase in order
        # to have it affect window related stuff
        loadPrcFile("Configrc.prc")

        builtins.userfiles = self.config.GetString('userfiles-directory')

        if not os.path.exists(userfiles):
            pathlib.Path(userfiles).mkdir(parents = True, exist_ok = True)

        # Check for -e or -d launch options
        parser = argparse.ArgumentParser(description = "Modes")
        parser.add_argument("--experimental", action = 'store_true', help = "Enables experimental features")
        parser.add_argument("--debug", action = 'store_true', help = "Enables debugging features")
        parser.add_argument("--noupdate", action = 'store_true', help = "Disables Auto Updating")

        parser.add_argument("--server", nargs = "*", help = "Enables features exclusive to various Toontown projects",
                            default = 'online')
        parser.add_argument("--holiday", nargs = "*", help = "Enables holiday modes. [halloween or winter]")
        parser.add_argument("--hoods", nargs = "*", help = "Only loads the storage files of the specified hoods",
                            default = ['TT', 'DD', 'BR', 'DG',
                                       'DL', 'MM', 'GS', 'GZ',
                                       'SBHQ', 'LBHQ', 'CBHQ', 'BBHQ',
                                       'OZ', 'PA', 'ES', 'TUT'])
        args = parser.parse_args()
        if args.experimental:
            loadPrcFileData("", "want-experimental true")
        if args.debug:
            loadPrcFileData("", "want-debug true")
            
        server = SERVER_TO_ID.get(args.server[0].lower(), DEFAULT_SERVER)
        self.server = server
            
        self.hoods = args.hoods
        # HACK: Check for dnaPath in args.hoods
        for hood in self.hoods[:]:
            if hood.endswith('.dna'):
                args.dnaPath = hood
                args.hoods.remove(hood)
                break
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
