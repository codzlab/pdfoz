@echo off

rem Set the name of the output directory
set OUTDIR=dist

rem Set the name of the executable
set EXECUTABLE=main.py

rem Set the name of the icon file
set ICONFILE=icon.png

rem Create the output directory if it doesn't exist
if not exist %OUTDIR% mkdir %OUTDIR%

rem Use pyinstaller to create the standalone executable
pyinstaller --onefile --noconsole --icon=%ICONFILE% %EXECUTABLE%

rem Clean up any temporary files
rd /s /q build
rd /s /q __pycache__

