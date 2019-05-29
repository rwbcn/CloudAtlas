#!/usr/bin/env python3
# Author: Ronny Wolf - BlueCat Networks

import time
import json
import configparser
import os
import bamclient as bam 

class config:
    def __init__(self, section, parameter, value):
        self.section = section
        self.parameter = parameter
        self.value = value


def cls():
    os.system('cls' if os.name == "nt" else "clear")


def setup():
    cls()
    print(bam.bcolours.GREEN + "######################################################" + bam.bcolours.ENDC)
    print(bam.bcolours.GREEN + "## Welcome to BlueCat CloudAtlas by Brian Shoreland ##" + bam.bcolours.ENDC)
    print(bam.bcolours.GREEN + "######################################################" + bam.bcolours.ENDC)
    time.sleep(0.5)
    print("")
    print("1) Configure BlueCat Address Manager")
    print("2) Configure Amazon Web Services")
    print("3) Configure Microsoft Azure")
    print("4) Configure Google Cloud Platform")
   # print("5) Configure Hyper-V Manager") -> Will be added in a future release
    print("6) Show configuration")
    print("7) Install prerequisits")
    print("8) Install as cronjob")
    print("9) Install Bluecat Gateway Workflow")
    print("0) Exit application")
    
    option = str(input(bam.bcolours.GREEN + "Please enter option: "))
    print("" + bam.bcolours.ENDC)
    if len(option) == 1:
        cls()
        switch(option)
    else:
        input(bam.bcolours.FAIL + "Wrong argument! Press ENTER and try again..." + bam.bcolours.ENDC)
        cls()
        setup()


def switch(option):
    if option == "1":     
        print(bam.bcolours.GREEN + "Bluecat Adress Manager Configuration" + bam.bcolours.ENDC)
        print("")
        bam_ip = str(input("Please enter your BlueCat Address Manager IP address: "))
        bam_api_user = str(input("Please enter your API user account: "))
        bam_api_password = str(input("Please enter your API user password: "))
        config_data = config('bam', ["bam_ip", "bam_api_user", "bam_api_password"], [bam_ip, bam_api_user, bam_api_password])
        config_write("cloudatlas.conf", config_data)
    elif option == "2":
        print(bam.bcolours.GREEN + "Amazon Web Services Configuration" + bam.bcolours.ENDC)
        print("")
        aws_region = str(input("Please enter your AWS region: "))
        aws_id = str(input("Please enter your AWS access key: "))
        aws_secretkey = str(input("Please enter your AWS secret key: "))
        config_data = config("aws", ["aws_region", "aws_id", "aws_secretkey"], [aws_region, aws_id, aws_secretkey])
        config_write("cloudatlas.conf", config_data)
    elif option == "3":
        print(bam.bcolours.GREEN + "Microsoft Azure Configuration" + bam.bcolours.ENDC)
        print("")
        azure_subscription = str(input("Please enter your Azure subscription: "))
        azure_client = str(input("Please enter your Azure client id: "))
        azure_client_secret = str(input("Please enter your Azure client secret: "))
        azure_tenant_id = str(input("Please enter your Azure tenant id: "))
        config_data = config("azure", ["azure_subscription", "azure_client", "azure_client_secret", "azure_tenant_id"], [azure_subscription, azure_client, azure_client_secret, azure_tenant_id])
        config_write("cloudatlas.conf", config_data)
    elif option == "4":
        print(bam.bcolours.GREEN + "Google Cloud Platform Configuration" + bam.bcolours.ENDC)
        print("")
        gcp_config_file = str(input("Please enter the path and filename to the GCP json file: "))
        config_data = config("gcp", ["gcp_config_file"], [gcp_config_file])
        config_write("cloudatlas.conf", config_data)        
    elif option == "6":
        show_configuration()


def config_write(configfile, config_data):
    parser = configparser.ConfigParser()
    parser.read(configfile)
    if parser.has_section(config_data.section):
        parser.remove_section(config_data.section)
    parser.add_section(config_data.section)
    parameter_count = 0
    while parameter_count <= len(config_data.parameter) - 1:
        parser.set(config_data.section, config_data.parameter[parameter_count], config_data.value[parameter_count])
        parameter_count += 1
    with open(configfile, "w") as configuration:
        parser.write(configuration)
    print("")
    input(bam.bcolours.GREEN + "Settings saved. Press Enter to continue...")
    cls()
    setup()


def config_read(configfile, section):
    parser = configparser.ConfigParser()
    parser.read(configfile)
    values = []
    if parser.has_section(section):
        parameters = parser.options(section)
    else:
        return 
    for parameter in parameters:
        values.append(parser.get(section, parameter))
    config_data = config(section, parameters, values)
    return config_data


def show_configuration():
    read_all = ["bam", "aws", "azure", "gcp"]
    for section in read_all:
        print("")
        config_data = config_read("cloudatlas.conf", section)
        if config_data is not None:
            parameter_count = 0
            print("[" + section + "]")
            while parameter_count <= len(config_data.parameter) - 1:
                print(config_data.parameter[parameter_count] + " = " + config_data.value[parameter_count])
                parameter_count += 1
            print("")
    input(bam.bcolours.GREEN + "Press Enter to continue...")
    cls()
    setup()


setup()
