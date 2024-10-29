# -*- coding: utf-8 -*-
"""
Arbitrage

Created on 27-oct-2024

@author: jaffolter

"""


import json
import requests
#import datetime as DT
#import time
#import pandas as pd
#import mysql.connector
#from datetime import datetime
#import configparser
import sys, os
import argparse
#from tabulate import tabulate


# Create the parser
# parser = argparse.ArgumentParser(description="Example argparse script")
parser = argparse.ArgumentParser(description='Process some token.')

# Add arguments
# parser.add_argument('filename', type=str, help="The name of the file to process")
parser.add_argument('--token', type=str, required=True, help='The token symbol')
parser.add_argument('--verbose', action='store_true', help="Increase output verbosity.")

# Parse the arguments
# args = parser.parse_args()




# Create the parser


# Add the --token argument


# Parse the arguments
args = parser.parse_args()

# Access the token symbol
symbol = args.token

# Print the token symbol
if args.verbose:
    print(f'The token symbol is: {symbol}')




def kraken(symbol,apisymbol,number):

    api_url = 'https://api.kraken.com/0/public/Ticker?pair={}'.format(apisymbol)
        
    res = response = requests.get(api_url)
    if args.verbose:
        print(f"API return code: {res.status_code}")

    if res.status_code == 200:

        obj = json.loads(response.text)

        data = f"obj['result']['{apisymbol}']['a'][0]"
        price = eval(data)
        sum = float(price) * float(number)
        print(f"{symbol},{apisymbol},{price},{sum},kraken")

    else:

        print(f"{symbol},{apisymbol},0,0,kraken")
     
    # return data


def coincodex(symbol,apisymbol,number):

    api_url = 'https://coincodex.com/api/coincodex/get_coin/{}'.format(apisymbol)

    res = response = requests.get(api_url)
    if args.verbose:
        print(f"API return code: {res.status_code}")

    if res.status_code == 200:

        obj = json.loads(response.text)

        price = float(obj['last_price_usd'])
        sum = float(price) * float(number)
        print(f"{symbol},{apisymbol},{price},{sum},coincodex")

    else:

        print(f"{symbol},{apisymbol},0,0,coincodex")
        

def kucoin(symbol,apisymbol,number):

    apisymbol = symbol + "-USDT"

    # symbol = 'BTC-USDT'
    api_url = 'https://api.kucoin.com/api/v1/market/orderbook/level1?symbol={}'.format(apisymbol)



    res = response = requests.get(api_url)
    if args.verbose:
        print(f"API return code: {res.status_code}")

    if res.status_code == 200:

        obj = json.loads(response.text)

        price = float(obj['data']['price'])
        sum = float(price) * float(number)
        print(f"{symbol},{apisymbol},{price},{sum},kucoin")


    else:

        print(f"{symbol},{apisymbol},0,0,kucoin")


def binance(symbol,apisymbol,number):

    # symbol = 'BTC-USDT'
    api_url = 'https://api.binance.com/api/v3/ticker/price?symbol={}'.format(apisymbol)

    res = response = requests.get(api_url)
    if args.verbose:
        print(f"API return code: {res.status_code}")

    if res.status_code == 200:

        obj = json.loads(response.text)

        price = float(obj['price'])
        sum = float(price) * float(number)
        print(f"{symbol},{apisymbol},{price},{sum},binance")

    else:

        print(f"{symbol},{apisymbol},0,0,binance")
  

def coinbase(symbol,apisymbol,number):

    # symbol = 'BTC-USDT'
    api_url = 'https://api.coinbase.com/v2/exchange-rates?currency={}'.format(apisymbol)

    res = response = requests.get(api_url)
    # print(res.status_code)


    if res.status_code == 200:

        obj = json.loads(response.text)

        price = float(obj['data']['rates']['USDT'])
        sum = float(price) * float(number)
        print(f"{symbol},{apisymbol},{price},{sum},coinbase")

    else:

        print(f"{symbol},{apisymbol},0,0,coinbase")


def bitfinex(symbol,apisymbol,number):

    # API documentation
    # https://docs.bitfinex.com/reference/rest-public-ticker

    # symbol = 'tXRPUSD'
    # api_url = 'https://api.coinbase.com/v2/exchange-rates?currency={}'.format(apisymbol)
    api_url = 'https://api-pub.bitfinex.com/v2/ticker/{}'.format(apisymbol)

    res = response = requests.get(api_url)
    # print(res.status_code)


    if res.status_code == 200:

        obj = json.loads(response.text)

        price = float(obj[6])
        sum = float(price) * float(number)
        print(f"{symbol},{apisymbol},{price},{sum},bitfinex")

    else:

        print(f"{symbol},{apisymbol},0,0,bitfinex")
  

def huobi(symbol,apisymbol,number):

    # API documentation
    # https://www.htx.com/en-us/opend/newApiPages/?id=7ec4aa2b-7773-11ed-9966-0242ac110003
    # https://api.huobi.pro/market/trade?symbol=xrpusdt

    api_url = 'https://api.huobi.pro/market/trade?symbol={}'.format(apisymbol)

    res = response = requests.get(api_url)
    if args.verbose:
        print(f"API return code: {res.status_code}")

    if res.status_code == 200:

        obj = json.loads(response.text)
        
        price = float(obj['tick']['data'][0]['price'])
        sum = price * float(number)
        print(f"{symbol},{apisymbol},{price},{sum},huobi")

    else:

        print(f"{symbol},{apisymbol},0,0,huobi")


def bithumb(symbol,apisymbol,number):

    # API documentation
    # https://apidocs.bithumb.com/reference/%ED%98%84%EC%9E%AC%EA%B0%80-%EC%A0%95%EB%B3%B4
    # https://api.huobi.pro/market/trade?symbol=xrpusdt

    api_url = 'https://api.huobi.pro/market/trade?symbol={}'.format(apisymbol)

    res = response = requests.get(api_url)
    if args.verbose:
        print(f"API return code: {res.status_code}")

    if res.status_code == 200:

        obj = json.loads(response.text)
        
        price = float(obj['tick']['data'][0]['price'])
        sum = price * float(number)
        print(f"{symbol},{apisymbol},{price},{sum},bithumb")

    else:

        print(f"{symbol},{apisymbol},0,0,bithumb")


def okx(symbol,apisymbol,number):


    # API documentation
    # https://www.okx.com/fr/okx-api
    # https://www.okx.com/docs-v5/en/#order-book-trading-market-data-get-tickers
    # https://www.okx.com/api/v5/market/ticker?instId=XRP-USDT
    # https://www.okx.com/api/v5/market/tickers?instType=SPOT

    api_url = 'https://www.okx.com/api/v5/market/ticker?instId={}'.format(apisymbol)

    res = response = requests.get(api_url)
    if args.verbose:
        print(f"API return code: {res.status_code}")

    if res.status_code == 200:

        obj = json.loads(response.text)
        
        price = obj['data'][0]['last']
        sum = float(price) * float(number)
        print(f"{symbol},{apisymbol},{price},{sum},okx")

    else:

        print(f"{symbol},{apisymbol},0,0,okx")


def gemini(symbol,apisymbol,number):

    # API documentation
    # https://docs.gemini.com/rest-api/?_gl=1*1yfvnhy*_gcl_au*MTI3MTYyNTE0OS4xNzMwMDUwMDc0#network
    # https://api.sandbox.gemini.com/v1/pubticker/XRPUSD


    api_url = 'https://api.sandbox.gemini.com/v1/pubticker/{}'.format(apisymbol)

    res = response = requests.get(api_url)
    if args.verbose:
        print(f"API return code: {res.status_code}")

    if res.status_code == 200:

        obj = json.loads(response.text)
        
        price = obj['ask']
        sum = float(price) * float(number)
        print(f"{symbol},{apisymbol},{price},{sum},gemini")

    else:

        print(f"{symbol},{apisymbol},0,0,gemini")



def poloniex(symbol,apisymbol,number):

    # API documentation
    # https://docs.legacy.poloniex.com/#returnticker

    api_url = 'https://api.sandbox.gemini.com/v1/pubticker/{}'.format(apisymbol)

    res = response = requests.get(api_url)
    if args.verbose:
        print(f"API return code: {res.status_code}")

    if res.status_code == 200:

        obj = json.loads(response.text)
        
        price = obj['ask']
        sum = float(price) * float(number)
        print(f"{symbol},{apisymbol},{price},{sum},poloniex")

    else:

        print(f"{symbol},{apisymbol},0,0,poloniex")





number=13000

# symbol='XRP'

apisymbol = symbol + "USDT"
#kraken(symbol,apisymbol,number)

apisymbol=symbol
#coincodex(symbol,apisymbol,number)

apisymbol = symbol + "-USDT"
#kucoin(symbol,apisymbol,number)

apisymbol = symbol + "USDT"
#binance(symbol,apisymbol,number)

apisymbol=symbol
#coinbase(symbol,apisymbol,number)

apisymbol="t"+symbol+"USD"
#bitfinex(symbol,apisymbol,number)

apisymbol = symbol + "USDT"
apisymbol = apisymbol.lower()
#huobi(symbol,apisymbol,number)

# not working yet
# bithumb(symbol,apisymbol,number)


apisymbol = symbol + "-USDT"
okx(symbol,apisymbol,number)


apisymbol=symbol+"USD"
gemini(symbol,apisymbol,number)


apisymbol=symbol+"USD"
poloniex(symbol,apisymbol,number)



# https://www.bitstamp.net/api/




'''
## Crypto exchanges
## work list

crypto exchange name, url, API
[X] Binance, https://www.binance.com, yes
[X] Coinbase, https://www.coinbase.com, yes
[X] Kraken, https://www.kraken.com, yes
[X] Bitfinex, https://www.bitfinex.com, yes
[X] Huobi, https://www.huobi.com, yes
[X] Bithumb, https://www.bithumb.com, yes
[X] OKEx, https://www.okex.com, yes
[X] Gemini, https://www.gemini.com, yes
[X] Poloniex, https://www.poloniex.com, yes
[X] KuCoin, https://www.kucoin.com, yes
[ ] Bitstamp, https://www.bitstamp.net, yes
[ ] Bittrex, https://www.bittrex.com, yes
[ ] Cex.io, https://www.cex.io, yes
[ ] Changelly, https://www.changelly.com, no
[ ] Coinmama, https://www.coinmama.com, no
[ ] Bybit, https://www.bybit.com, yes
[ ] Gate.io, https://www.gate.io, yes
[ ] Bitso, https://www.bitso.com, yes
[ ] Liquid, https://www.liquid.com, yes
[ ] Coincheck, https://coincheck.com, yes
[ ] Binance US, https://www.binance.us, yes
[ ] Crypto.com Exchange, https://exchange.crypto.com, yes
[ ] Phemex, https://www.phemex.com, yes
[ ] CoinEx, https://www.coinex.com, yes
[ ] Upbit, https://upbit.com, yes
[ ] BTSE, https://www.btse.com, yes
[ ] MEXC, https://www.mexc.com, yes
'''