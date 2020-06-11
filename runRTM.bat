@echo off
set PATH=%PATH%;lib
set TTMODELS=.
set DMODELS=.
set CFG_PATH=.
set CONFIG_CONFIG=:configpath=CFG_PATH
python.exe -m toontown.toon.RobotToonManager
pause