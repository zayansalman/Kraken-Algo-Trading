import krakenex
import pandas as pd
from pykrakenapi import KrakenAPI
from time import sleep
import plotly.graph_objects as go
import plotly.express as px

api = krakenex.API()
kraken = KrakenAPI(api)

# api.load_key('kraken_api_keys.txt')


def get_ticker_info(pair):
    ticker = kraken.get_ticker_information(pair)
    return ticker.T


def get_ohlc_data_in_chart(pair):
    ohlc_data = kraken.get_ohlc_data(pair, interval=1440, ascending=True)
    ohlc_data[0].head()
    ohlc_data[0]['20 SMA'] = ohlc_data[0]['close'].rolling(20).mean()
    ohlc_data[0].tail()

    fig = go.Figure(data=[go.Candlestick(x=ohlc_data[0].index,
                                         open=ohlc_data[0]['open'],
                                         high=ohlc_data[0]['high'],
                                         low=ohlc_data[0]['low'],
                                         close=ohlc_data[0]['close'],
                                         ),
                          go.Scatter(x=ohlc_data[0].index, y=ohlc_data[0]['20 SMA'],
                                     line=dict(color='purple', width=1))])
    fig.show()


def get_order_book(pair, count=20):
    book = kraken.get_order_book(pair, count)
    pair_df = pd.merge(book[0], book[1], left_index=True, right_index=True)
    pair_df.rename({"price_x": "Bid Price", "volume_x": "Bid Amount", "time_x": "Bid Time", "price_y": "Ask Price",
                    "volume_y": "Ask Amount", "time_y": "Ask Time"}, axis='columns')
    return pair_df


def send_market_order(pair, order_type, volume):
    currency_price = float((kraken.get_ticker_information(pair))['a'][0][0])
    print(currency_price)
    response = kraken.add_standard_order(pair=pair, type=order_type, ordertype='market', volume=volume, validate=False)
    sleep(3)
    check_order = kraken.query_orders_info(response['txid'][0])
    if check_order['status'][0] == 'open' or 'closed':
        print('Order executed')
    else:
        print('Order failed')


if __name__ == '__main__':
    # asset_info = kraken.get_asset_info()
    # tradable_pairs_info = kraken.get_tradable_asset_pairs()
    # btcusd = get_ticker_info('BTCUSD')
    # get_ohlc_data_in_chart('BTCUSD')
    # help(KrakenAPI)
    print('debug')
