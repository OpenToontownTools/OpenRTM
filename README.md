# Open Robot Toon Manager (RTM)
## About RobotToon ##
RobotToon was a development tool for Disney's Toontown Online artists to create scenes for backgrounds to be used as wallpapers, blog posts, and various graphic design related assets. OpenRTM is an open source project aimed to update the RTM to be compatible with the latest verisons of Panda3D, Python 3, and with feature improvements.

## Requirements
### ***IMPORTANT***
* **You need a Panda3D build that INCLUDES commit [b507c88](https://github.com/panda3d/panda3d/commit/b507c88cd9fd5d3a432aae42fdc9165422a527b4) and [7d14d52](https://github.com/panda3d/panda3d/commit/7d14d5275c826b5d02486b0d12eae5f0f9b6a2c6) as these are CRITICAL fixes for the editor. You will NOT be able to use it without this fix!**
* Toontown phase files that include all the dna files. [These](https://github.com/open-toontown/resources) work fine. ***Toontown Rewritten's phase files do NOT contain .dna files since they use a completely different format, so you need to use them from elsewhere. Open-Toontown's resources are the closest to Toontown Online's that you can get, while also being completely updated and compatible with Panda3d 1.10.***
* Here you have two options:
    * The advanced option
        * Build yourself a copy of [libtoontown](https://github.com/OpenToontownTools/libtoontown), and drop the .pyd files in the root directory.
        * Recent Panda3D build (1.10.7 or later) running on *__Python 3__*. This editor is NOT compatible with Python 2.x and will NOT ever be made compatible as Python 2.x is no longer supported.
    * **OR** the easy option:
        * you can download [my copy](https://drive.google.com/file/d/1lJ-4Ce3qLvRnvZzHCPlXAM088pCK7qr2/view?usp=sharing) of panda with the compatible libtoontown files in there. Just drag Panda3D-1.11.0-Py39-x64 to your C drive root directory and the libotp.pyd and libtoontown.pyd files to the root level editor directory. Note that the PYD files in here are ONLY compatible with MY copy of panda, so if you are using any other build you have to rebuild them yourself.

~~### You can also pick up a pre-built build in the releases tab~~ *Coming Soon*

## Credits
* [Disyer](https://github.com/darktohka/) - Project Lead | Developer
* [Loonatic](https://github.com/loonaticx/) - Project Lead | Developer
* [drewcification](https://github.com/drewc5131) - Open Toontown Tools Project Lead | Developer
* [Any other contributors are listed on the side](https://github.com/OpenToontownTools/OpenRTM/graphs/contributors)

# FAQ

### Some of my props are using textures as if they were in a different playground?
* This is OK. This is just because you have support for more than 1 playground loaded. This is only visible in the editor, but I recommend you only load the zone you are working on.

### I did the setup properly, but the editor just closes on startup with no error message, how do I fix?
* If you are downloading my redistributed copy of Panda from above, this may be an issue of having multiple installations of panda, and an incorrect one being targeted. Try one or both of the following:
    * Edit the registry
        * Open RegEdit
        * Navigate to `Computer\HKEY_CURRENT_USER\SOFTWARE\Python\PythonCore\3.9\InstallPath`
        * Change (Default)'s value to `C:\Panda3D-1.11.0-py39-x64\python`
        * Change ExecutablePath's value to `C:\Panda3D-1.11.0-py39-x64\python\python.exe`
        * Save, and if that does not work try restarting your PC, or doing option #2
    * Remove all other versions of Panda3D.
