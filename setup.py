#!/usr/bin/env python3
# Author: Ronny Wolf - BlueCat Networks

import time
import json

def setup():
    print("")
    print("################################################")
    print("Welcome to BlueCat CloudAtlas by Brian Shoreland")
    print("################################################")
    time.sleep(2)
    print("")
    print("1) Configure BlueCat Address Manager")
    print("2) Configure Amazon Web Services")
    print("3) Configure Microsoft Azure")
    print("4) Configure Google Cloud Platform")
    print("7) Install prerequisits")
    print("8) Create Bluecat Gateway Workflow")
    print("0) Exit application")
    option = str(input("Please enter option: "))
    if len(option) == 1:
        switch(option)
    else:
        print("Wrong argument! Try again")
        print("")
        time.sleep(2)
        setup()


def switch(option):
    if option == "1":
        bam_ip = str(input("Please enter your BlueCat Address Manager IP address: "))
        bam_api_user = str(input("Please enter your API user account: "))
        bam_api_password = str(input("Please enter your API user password: "))
        with open('config.json'. 'w') as outfile:
            json.dump(bam_ip, outfile)
        print(bam_ip)
        print(bam_api_user)
        print(bam_api_password)

     
setup()
