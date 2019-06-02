#!/usr/bin/env python3
# Author: Ronny Wolf - BlueCat Networks

import sys

try:
    assert sys.version_info >= (3, 0)
except:
    print("\033[91mError: Wrong version (" + str(sys.version_info.major) + "." + str(sys.version_info.minor) + "), please use Python 3.x! \033[0m")
    exit()

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


def install_modules(package):
    import subprocess
    import sys
    print(bam.bcolours.GREEN + "########### Package: " + package + " ########### " + bam.bcolours.ENDC)
    subprocess.call([sys.executable, "-m", "pip", "install", package])
    print(bam.bcolours.GREEN + "########### Package: " + package + " finished ########### " + bam.bcolours.ENDC)
    time.sleep(0.5)

def cls():
    os.system('cls' if os.name == "nt" else "clear")

def setup():
    cls()
    print(bam.bcolours.GREEN + "#####################################################" + bam.bcolours.ENDC)
    print(bam.bcolours.GREEN + "## Welcome to BlueCat CloudAtlas by Brian Shorland ##" + bam.bcolours.ENDC)
    print(bam.bcolours.GREEN + "#####################################################" + bam.bcolours.ENDC)
    time.sleep(0.5)
    print("")
    print("1) Configure BlueCat Address Manager")
    print("2) Configure Amazon Web Services")
    print("3) Configure Microsoft Azure")
    print("4) Configure Google Cloud Platform")
    print("5) Run BlueCat CloudAtlas")
    print("6) Show configuration")
    print("7) Install prerequisits")
    print("8) Install as cronjob")
    print("9) Install Bluecat Gateway Workflow")
    print("0) Exit application")
    
    option = str(input(bam.bcolours.GREEN + "Please enter option: "))
    print("" + bam.bcolours.ENDC)
    if len(option) == 1:
        cls()
        switch_main(option)
    else:
        input(bam.bcolours.FAIL + "Wrong argument! Press ENTER and try again..." + bam.bcolours.ENDC)
        cls()
        setup()


def switch_main(option):
    if option == "1":     
        print(bam.bcolours.GREEN + "Bluecat Adress Manager Configuration" + bam.bcolours.ENDC)
        print("")
        bam_ip = str(input("Please enter your BlueCat Address Manager IP address: "))
        bam_api_user = str(input("Please enter your API user account: "))
        bam_api_password = str(input("Please enter your API user password: "))
        bam_config_name = str(input("Please enter your configuration name: "))
        config_data = config('bam', ["bam_ip", "bam_api_user", "bam_api_password", "bam_config_name"], [bam_ip, bam_api_user, bam_api_password, bam_config_name])
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
    elif option == "5":
        print(bam.bcolours.GREEN + "Run BlueCat CloudAtlas" + bam.bcolours.ENDC)
        print("1) Run Amazon Web Service Integration")
        print("2) Run Microsoft Integration")
        print("3) Run Google Cloud Platform Integration")
        print("0) Return to main menu...")
        option = str(input(bam.bcolours.GREEN + "Please enter option: "))
        print("" + bam.bcolours.ENDC)
        if len(option) == 1:
            cls()
            switch_run(option)
        else:
            input(bam.bcolours.FAIL + "Wrong argument! Press ENTER and try again..." + bam.bcolours.ENDC)
            cls()
            switch_main("5")
    elif option == "6":
        show_configuration()
    elif option == "7":
        packages = ["google", "boto3", "configparser", "azure", "datetime", "google-api-python-client", "oauthlib", "netaddr", "pprint"]
        for pkg in packages:
            install_modules(pkg)
        print("")
        input(bam.bcolours.GREEN + "Prerequistis installed. Press Enter to get back to main..." + bam.bcolours.ENDC)
        setup()
    elif option == "0":
        exit()


def switch_run(option):
    if option == "1": 
        bam_config = config_read("cloudatlas.conf", "bam")
        aws_config = config_read("cloudatlas.conf", "aws")
        import cloudatlas_aws as aws
        aws.cloudatlas_aws(aws_config.value, bam_config.value)
    elif option == "2":
        print("Run Azure")
    elif option == "3":
        print("Run GCP")
    elif option == "0":
        cls()
        setup()


def config_cronjob():
    import python_crontab



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
        config_data = None
        for parameter in parameters:
            values.append(parser.get(section, parameter))
            config_data = config(section, parameters, values)
        return config_data
    else:
        print(bam.bcolours.FAIL + "Config not existing. Please configure " + section + " configuration..." + bam.bcolours.ENDC)
        print("")
        if section == "bam":
            switch_main("1")
        elif section == "aws":
            switch_main("2")
        elif section == "azure":
            switch_main("3")
        elif section == "gcp":
            switch_main("4")
    

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
