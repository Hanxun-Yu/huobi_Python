
from huobi.client.market import MarketClient
from huobi.constant import *
from huobi.exception.huobi_api_exception import HuobiApiException
from huobi.model.market import MarketTicker
from huobi.model.market.candlestick_event import CandlestickEvent


def callback(candlestick_event: 'CandlestickEvent'):
    candlestick_event.print_object()
    print("\n")


def error(e: 'HuobiApiException'):
    print(e.error_code + e.error_message)

# market_client = MarketClient()
# market_client.sub_candlestick("btcusdt,ethusdt", CandlestickInterval.MIN5, callback, error)
# market_client.sub_candlestick("btcusdt", CandlestickInterval.MIN5, callback, error)
# market_client.sub_candlestick("ethusdt", CandlestickInterval.MIN1, callback, error)

sub_client = MarketClient(init_log=False)
list_obj = sub_client.get_market_tickers()

list_obj.sort(key=lambda x: x.count, reverse=True)

list_obj = list_obj[0:100]
ret = []
for obj in list_obj:
    obj: MarketTicker = obj
    if obj.symbol.endswith("usdt"):
        ret.append(obj)
    # else:
    #     print(obj.symbol +" code not found!")
    # print(obj.symbol)

ret.sort(key=lambda x: x.count, reverse=True)

str = ""
for obj in ret:
    obj: MarketTicker = obj
    str += obj.symbol
    str += ","

sub_client.sub_candlestick(str, CandlestickInterval.MIN1, callback, error)

