#!/usr/bin/env python3
# Author: Ronny Wolf - BlueCat Networks

import time
import json
import configparser

class config:
    def __init__(self, section, parameter, value):
        self.section = section
        self.parameter = parameter
        self.value = value


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
        config_data = config('bam', ["bam_ip", "bam_api_user", "bam_api_password"], [bam_ip, bam_api_user, bam_api_password])
        config_write("cloudatlas.conf", config_data)
    elif option == "2":
        aws_region = str(input("Please enter your AWS region: "))
        aws_id = str(input("Please enter your AWS access key: "))
        aws_secretkey = str(input("Please enter your AWS secret key: "))
        config_data = config("aws", ["aws_region", "aws_id", "aws_secretkey"], [aws_region, aws_id, aws_secretkey])
        config_write("cloudatlas.conf", config_data)

    elif option == "3":
        azure_subscription = str(input("Please enter your Azure subscription: "))
        azure_client = str(input("Please enter your Azure client id: "))
        azure_client_secret = str(input("Please enter your Azure client secret: "))
        azure_tenant_id = str(input("Please enter your Azure tenant id: "))
        config_data = config("azure", ["azure_subscription", "azure_client", "azure_client_secret", "azure_tenant_id"], [azure_subscription, azure_client, azure_client_secret, azure_tenant_id])
        config_write("cloudatlas.conf", config_data)
    elif option == "4":
        gcp_config_file = str(input("Please enter the path and filename to the GCP json file: "))
        config_data = config("gcp", ["gcp_config_file"], [gcp_config_file])
        config_write("cloudatlas.conf", config_data)


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


def config_read(configfile, data):
    print("something")


setup()
