@echo off
:main
cls
netsh wlan show profile
set /p user_profile=Select a user profile (or type 'E' to exit): 
if "%user_profile%"=="E" (
    exit 0
)
netsh wlan show profile %user_profile% key=clear
pause
goto :main
