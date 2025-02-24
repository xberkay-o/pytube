@echo off

rem 
set "libraries=os pytube colorama"

rem 
for %%i in (%libraries%) do (
    python -c "import %%i" >nul 2>&1
    if errorlevel 1 (
        echo %%i library not found. Downloading...
        pip install %%i
    ) else (
        echo %%i library already installed.
    )
)

echo Process completed.
pause
