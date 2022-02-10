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
    add_current_price_col(trade_history_df)
    trade_history_df['% change'] = percentage_change(trade_history_df['price'], trade_history_df['current price'])
    return trade_history_df


def percentage_change(col1, col2):
    return ((col2 - col1)/col1) * 100


def add_current_price_col(df):
    pair_col_list = df['pair']
    curr_price_col = create_curr_price_col(pair_col_list)
    curr_price_col = [float(x) for x in curr_price_col]
    df['current price'] = curr_price_col


def create_curr_price_col(pair_col_list):
    curr_price_list = list()
    for pair in pair_col_list:
        curr_price = get_pair_current_price(pair)
        curr_price_list.append(curr_price)
    return curr_price_list


def get_pair_current_price(pair):
    df = kraken.get_ticker_information(pair=pair)
    df = df.rename(columns={'a': 'ask', 'b': 'bid', 'c': 'last trade(price/vol)', 'v': 'vol(today/24h)', 'p': 'vwap24h(today/24h)', 't': 'no. of trades(today/24h)',
                            'l': 'low(today/24h)', 'h': 'high(today/24h)', 'o': 'open'})
    return df['last trade(price/vol)'][0][0]


if __name__ == '__main__':
    # trade_df = pd.DataFrame(kraken.get_trades_history()[0])
    df1 = create_pnl_df()

    print('debug')
