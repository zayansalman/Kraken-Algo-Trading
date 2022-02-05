import krakenex
from pykrakenapi import KrakenAPI
import pandas as pd

api = krakenex.API()
kraken = KrakenAPI(api)
api.load_key('kraken_api_keys.txt')


def create_pnl_df():
    trade_history_df = pd.DataFrame(kraken.get_trades_history()[0])
    trade_history_df = trade_history_df.reset_index()
    trade_history_df.drop(trade_history_df.tail(2).index, inplace=True)
    c_type = trade_history_df.loc[:, 'type'] == 'buy'
    trade_history_df = trade_history_df.loc[c_type]
    trade_history_df = trade_history_df.loc[:, ['pair', 'price', 'cost', 'fee', 'vol']]


def add_current_price_col(df):
    pass


def get_pair_current_price(pair):
    df = kraken.get_ticker_information(pair=pair).T
    df = df.rename(index={'a': 'ask', 'b': 'bid', 'c': 'last trade(price/vol)', 'v': 'vol(today/24h)', 'p': 'vwap24h(today/24h)', 't': 'no. of trades(today/24h)',
                          'l': 'low(today/24h)', 'h': 'high(today/24h)', 'o': 'open'})


if __name__ == '__main__':
    trade_history_df = pd.DataFrame(kraken.get_trades_history()[0])
    print('debug')
