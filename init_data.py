
import numpy as np
import pandas as pd
import tushare as ts
import time
import codecs
from datetime import date, timedelta



ts_token="46dc6393e4bee0a19b34625a8292d258827f2d4c62777e11cd5f0998"
stock_file = "./data/stock.list.txt"

def get_open_date_list(s_date, e_date):
    ts.set_token(ts_token)
    pro = ts.pro_api()
    df = pro.trade_cal(exchange='SSE', is_open='1',
                            start_date=s_date,
                            end_date=e_date,
                            fields='cal_date')
    return df['cal_date'].tolist()


def update_all_stock():
    today = date.today().strftime("%Y%m%d")
    before_day = (date.today() + timedelta(days=-200)).strftime("%Y%m%d")
    day_list = get_open_date_list(before_day, today)
    must_start_day = day_list[-100]


    ts.set_token(ts_token)
    pro = ts.pro_api()
    data = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')

    with codecs.open(stock_file, 'w', 'utf-8') as fw:
        for i in range(len(data)):
            out_str = "{}\t{}\t{}\t{}\t{}\t{}\n".format(data['ts_code'][i], data['symbol'][i],
                                                        data['name'][i], data['area'][i], data['industry'][i],
                                                        data['list_date'][i],)
            if data['name'][i].find("ST") == -1:
                if int(must_start_day) > int(data['list_date'][i]):
                    fw.write(out_str)


'''

codes = ['000001',]

data = ts.get_realtime_quotes(codes)
print(data['price'].values[0])

df = pro.daily(trade_date='20220609')
for name in df:
    print(name)
'''

def init_data(s_date, e_date):
    date_list = get_open_date_list(s_date, e_date)

    for date_str in date_list:
        ts.pro_bar()
    pro = ts.pro_api(ts_token)
    pass

def test():
    ts.set_token(ts_token)
    pro = ts.pro_api()
    df = pro.query('daily_basic', ts_code='', trade_date='20180726',fields='ts_code,trade_date,turnover_rate,volume_ratio,pe,pb')
    print(df)

if __name__ == "__main__":
    test()
    #get_open_date_list('20220101', '20220610')