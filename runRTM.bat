@echo off
set PATH=%PATH%;lib
set TTMODELS=.
set DMODELS=.
set CFG_PATH=.
set CONFIG_CONFIG=:configpath=CFG_PATH
"C:\Panda3D-1.11.0-py37-x64\python\python.exe" -m toontown.toon.RobotToonManager
pause