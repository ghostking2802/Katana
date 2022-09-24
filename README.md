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
-->Chrome.py=>File responsible for extracting chrome cache
-->Chrome_receive,py=>File responsible for recieving the chrome cache in ttacker machine
-->backdoor.py=>File to spawn cmd shell in victim machine
-->stream.py=>Responsible for getting webcam stream and send the feed over UDP to attacker machine
-->test.py=>Responsible for handling webcam feed on attacker machine
