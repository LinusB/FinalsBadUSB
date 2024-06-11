# BadUSB
# Project Overview
This project, part of the IT-Security final project at Hanyang University, demonstrates a sophisticated attack vector leveraging physical access and USB manipulation. The core concept is the creation of a BadUSB device that, when plugged into a Windows system, exploits the system's unlocked state. Additionally, a phishing website is deployed to enhance the attack's effectiveness. This project is intended solely for academic purposes.

# Repository Structure
initialCode.py: The initial script executed when the USB is plugged in.<br /><br />
src/attack.cmd: Shortcut to the attackingScript.cmd file. When executed it opens the terminal minimized.<br /><br />
src/attackingScript.cmd:  The script that initiates the attack using a Batchfile.<br /><br />
src/get_user_email.ps1: A PowerShell script to gather user email data.<br /><br />
src/upload.py: Python script for data processing and uploading to a specified webserver.<br /><br />
phising/kakaoLoginPage.html: The Kakao Login phishing website to capture login credentials. This is deployed on a webserver<br /><br />

# Workflow
Initial Execution: The initialCode.py is executed upon plugging in the USB.<br /><br />
Attack Initiation: This script triggers attack.cmd located in the /src/ directory.<br /><br />
Data Gathering: The attack script collects the 1. personal information using the Powershell file get_user_email.ps1. that gathers email informations, 2. hostsystem informations and networkinterfaces and 3. SSIDs + passwords of WLAN configurations that are locally stored.<br /><br />
Data Upload: Collected data is uploaded to a specified web server hosting the phishing website.<br /><br />
Credential Capture: The phishing website (kakaoLoginPage.html) captures login credentials.<br /><br />

# Usage Instructions
Setup USB: Copy initialCode.py and the src folder to the USB drive. Rename the src folder to .temp (that it seems like a temporary folder created by the USB).<br /><br />
Deploy Phishing Site: Host the kakaoLoginPage.html on your web server.<br /><br />
Execute: Plug the USB into the target Windows system.<br /><br />

# Security Notice
This project is for educational purposes only. Unauthorized use of this software to compromise systems without permission is illegal!!<br />

# Contributions
For changes, please open an issue to discuss your proposed modifications.

# License
This project is licensed under the MIT License.<br /><br />

For more details, visit the GitHub repository.

