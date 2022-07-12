import easytrader
import easyquotation
import json


class Trader():
    def __init__(self):
        self.user = easytrader.use('gj_client')
        self.user.connect(r'')

        self.quotation = easyquotation.use('sina')

    def get_balance(self):
        data = self.user.balance
        data_dict = json.loads(data)
        if len(data_dict) > 0:
            remain_money = data_dict[0]['可用资金']
            total_money = data_dict[0]['总资产']
            return remain_money, total_money
        return -1, -1

    def stock_holding_cost(self, stock_code):
        holding_data = self.user.position
        hdata_dict = json.loads(holding_data)
        for d in hdata_dict:
            if d["证券代码"] == stock_code:
                return d['参考成本价'], d['当前持仓'], d['盈亏比例(%)']
        # not find
        return -1


    def buy(self, stock_code, price, amount):
        return self.user.buy(stock_code, price, amount)


    def sell(self, stock_code, price, amount):
        return self.user.sell(stock_code, price, amount)


    def get_zt_price(self, stock_code):
        d = self.quotation.real(stock_code)

        pass

    def get_dt_price(self, stock_code):
        d = self.quotation.real(stock_code)
        pass





if __name__ == "__main__":
    jsonData = '[{"参考市值":1,"可用资金":2,"总资产":3,"股份参考盈亏":4,"资金余额":5}]'
    #jsonData = "[{'参考市值': 21642.0,  '可用资金': 28494.21,  '币种': '0',  '总资产': 50136.21,  '股份参考盈亏': -90.21,  '资金余额': 28494.21,  '资金帐号': 'xxx'}]"
    #d = json.loads(jsonData)
    d = json.loads(jsonData)

    print(d[0])