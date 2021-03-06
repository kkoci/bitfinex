import os, sys
from datetime import datetime

import bitfinex

# symbol to query the order book
symbol = 'btcusd'

# set the parameters to limit the number of bids or asks
parameters = {'limit_asks': 5, 'limit_bids': 5}

# create the client
client = bitfinex.Client()

while True:

    # get latest ticker
    ticker = client.ticker(symbol)

    # get the order book
    orders = client.order_book(symbol, parameters)

    # clear the display, and update values
    os.system('clear')

    print("# Bitfinex (Last Update : %s)" % (datetime.now()))
    print("## Last Ticker")
    print(ticker)

    for order_type in orders:
        print("")
        print("%s %s" % ("## ", order_type))
        for order in orders[order_type]:
            print order
