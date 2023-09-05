:: Program : BAFI
:: Description : Collect information about WI-FI profiles stored on the computer.
:: Author : R0P1
:: Github: https://github.com/R0P1/bafi.git

@echo off
:main
cls
echo.
echo ----------------------------- BAFI -----------------------------                                                                                                 
echo Collect information about WI-FI profiles stored on the computer.
echo ----------------------------------------------------------------
echo                                 https://github.com/r0p1/bafi.git
netsh wlan show profile
SET /p user_profile="[BAFI] Select a user profile (or type 'E' to exit):" 
if %user_profile%=="E" (
    exit /b 0
)
netsh wlan show profile %user_profile% key=clear
pause
goto :main
