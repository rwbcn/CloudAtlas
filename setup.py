#!/usr/bin/env python3
# Author: Ronny Wolf - BlueCat Networks

import time
import json
import configparser

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
    print("8) Install as cronjob")
    print("9) Create Bluecat Gateway Workflow")
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
        config_write("test.json", "data")
    elif option == "2":
        aws_region = str(input("Please enter your AWS region: "))
        aws_id = str(input("Please enter your AWS access key: "))
        aws_secretkey = str(input("Please enter your AWS secret key: "))
        config_write("test.json", "data")
    elif option == "3":
        azure_subscription = str(input("Please enter your Azure subscription: "))
        azure_client = str(input("Please enter your Azure client id: "))
        azure_client_secret = str(input("Please enter your Azure client secret: "))
        azure_tenant_id = str(input("Please enter your Azure tenant id: "))
        config_write("test.json", "data")
    elif option == "4":
        gcp_config_file = str(input("Please enter the path and filename to the GCP json file: "))
        config_write("test.json", "data")


def config_write(configfile, data):
    print("Do some work")

def config_read(configfile, data):
    print("Do some other work")
     
setup()
