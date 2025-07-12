@echo off
echo Starting Jekyll Compose - Modern Edition...
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.6+ and try again
    pause
    exit /b 1
)

REM Install dependencies if needed
if not exist ".jekyll_gui_deps_installed" (
    echo Installing dependencies...
    pip install pyyaml >nul 2>&1
    echo. > .jekyll_gui_deps_installed
)

REM Start the modern GUI
python jekyll_compose_modern.py

if errorlevel 1 (
    echo.
    echo An error occurred while running the application.
    pause
)
