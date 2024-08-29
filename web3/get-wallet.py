# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 21:52:18 2023

@author: jaffolter
"""
# from datetime import datetime


# read wallet addresses stored an excel file and return the balance.
# 
# Excel file name : invest.xlsm (can be whatever you want, change the code!)
# Sheet name : wallets          (can be whatever you want, change the code!)
#
# Sheet format 
# =====================
# keep these header in row1 otherwise it will fails
# 4 first columns are mandatories !!!
# 
# Address,Chain,Type,Exchange,comment
# [Your Wallet Address],ETH,Wallet,[Your Exchange],[Your comment]



# documentation
#
# XRP API 
# https://docs.xrpscan.com/api-documentation/introduction
#
# BTC API 
#  https://...
#
# ETH API 
# https://etherscan.io/apis

# for Ethereum you need an API key, mandatory !

import json
import requests
import datetime as DT
# import time
import pandas as pd
import configparser
import sys, os


# -------------------------------------
# read config file and get parameters section

config = configparser.ConfigParser()

ini_path = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])),'get-wallet.ini')

# old ini_path
# ini_path = os.path.join(os.getcwd(),'pdf2image-ext.ini')

config.read(ini_path)
# print(ini_path)

# get data from config file (.ini)
api_key_eth = config.get('settings','api_key_eth')
excel_file = config.get('settings','excel_file')
excel_sheet = config.get('settings','excel_sheet')
csv_outfile = config.get('settings','csv_outfile')


def generate_wallet_list():

    # print("Generate token list from Excel")
    # df = pd.read_excel(r'G:\Mon Drive\finance\invest.xlsm', sheet_name='wallets', header=0)
    df = pd.read_excel(excel_file, sheet_name=excel_sheet, header=0)

    # uncomment for storage in CSV file
    fout = open(csv_outfile, 'w')

    #drop columns by index in-place
    df.drop(df.columns[[4]],axis=1, inplace=True)

    for index, row in df.iterrows():  

        mytype=str(row['Type']) + str(row['Chain'])
        # treat only wallet

        match mytype:

            case 'WalletXRP':

                myaddress=str(row['Address'])
                # call the API with address and return adjusted balance
                balance = API_call_XRP_address(myaddress)
 
            case 'WalletBTC':
                # call the API with address and return adjusted balance
                myaddress=str(row['Address'])
                balance = API_call_BTC_address(myaddress)

            case 'WalletETH':
                # call the API with address and return adjusted balance
                myaddress=str(row['Address'])
                balance = API_call_ETH_address(myaddress)

            case _:
                # print('This is a SPOT address ', row['Address'])
                continue

        mytime=DT.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(mytime + "," + str(row['Chain']) + "," + str(row['Exchange']) + "," + myaddress + "," + str(balance))

        # uncomment for storage in CSV file
        fout.writelines(mytime + "," + str(row['Chain']) + "," + str(row['Exchange']) + "," + myaddress + "," + str(balance)+"\n")

    # uncomment for storage in CSV file
    fout.close()



# API call on xrpscan
# balance does not need to be adjusted

def API_call_XRP_address(myaddress):
        
        api_url = 'https://api.xrpscan.com/api/v1/account/{}'.format(myaddress)

        res = response = requests.get(api_url)

        if res.status_code == 200:

            obj = json.loads(response.text)
            balance = float(obj['xrpBalance'])

        else:

            balance='0'

        return balance


# API call on blockstream
# balance must be adjusted, divide by 100000000

def API_call_BTC_address(myaddress):
   
        api_url = 'https://blockstream.info/api/address/{}'.format(myaddress)

        res = response = requests.get(api_url)

        if res.status_code == 200:

            obj = json.loads(response.text)
            balance = obj['chain_stats']['funded_txo_sum']

        else:

            balance='0'

        # balance adjustment 

        balance=balance/100000000
        return balance


# API call on etherscan
# balance must be adjusted, divide by 1000000000000000000

def API_call_ETH_address(myaddress):
   
        api_url = 'https://api.etherscan.io/api?module=account&action=balance&address={}&tag=latest&apikey={}'.format(myaddress,api_key_eth)

        res = response = requests.get(api_url)

        if res.status_code == 200:

            obj = json.loads(response.text)
            balance = int(obj['result'])

        else:

            balance='0'

        # balance adjustment 

        balance=balance/1000000000000000000
        return balance

generate_wallet_list()







