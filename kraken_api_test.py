import krakenex
import pandas as pd
from pykrakenapi import KrakenAPI

import plotly.graph_objects as go
import plotly.express as px

api = krakenex.API()
k = KrakenAPI(api)

# asset_info = k.get_asset_info()
#
# tradable_pairs_info = k.get_tradable_asset_pairs()
#
# ticker = k.get_ticker_information('BTCUSD')
# ticker_info = ticker.T

# historical_data = k.get_ohlc_data('BTCUSD', interval=1440, ascending=True)
# historical_data[0].head()
# historical_data[0]['20 SMA'] = historical_data[0]['close'].rolling(20).mean()
# historical_data[0].tail()
#
# fig = go.Figure(data=[go.Candlestick(x=historical_data[0].index,
#                                      open=historical_data[0]['open'],
#                                      high=historical_data[0]['high'],
#                                      low=historical_data[0]['low'],
#                                      close=historical_data[0]['close'],
#                                      ),
#                       go.Scatter(x=historical_data[0].index, y=historical_data[0]['20 SMA'],
#                                  line=dict(color='purple', width=1))])
# fig.show()

# book = k.get_order_book('ETHUSD', count=20)
# eth_df = pd.merge(book[0], book[1], left_index=True, right_index=True)
# eth_df = eth_df.rename({"price_x": "Bid Price", "volume_x": "Bid Amount", "time_x": "Bid Time", "price_y": "Ask Price",
#                         "volume_y": "Ask Amount", "time_y": "Ask Time"}, axis='columns')



print('debug')
