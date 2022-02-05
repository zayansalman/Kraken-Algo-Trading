import krakenex
from pykrakenapi import KrakenAPI
import pandas as pd

api = krakenex.API()
kraken = KrakenAPI(api)
api.load_key('kraken_api_keys.txt')


def get_ledgers():
    return pd.DataFrame(kraken.get_ledgers_info()[0])


def get_trades_history():
    return pd.DataFrame(kraken.get_trades_history()[0])


if __name__ == '__main__':
    df = kraken.get_open_positions()
    print('debug')