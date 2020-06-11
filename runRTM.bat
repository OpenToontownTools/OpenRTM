@echo off
set PATH=lib
set PYTHONPATH=.;lib-tk
set TTMODELS=.
set DMODELS=.
set CFG_PATH=.
set CONFIG_CONFIG=:configpath=CFG_PATH
python -i toontown/toon/RobotToonManager.py
pause