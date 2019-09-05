import pandas as pd

def everyday(data, nation, begin, end):
    """
    欲しい通貨のデータを返す
    Parameters
    ----------
    data : pandas DataFrame
        必要なデータ
    nation : chr
        欲しいデータの通貨名
    begin : int
        欲しいデータの開始日
    end : int
        欲しいデータの最終日 + 1

    Return
    ------
    everyday : pandas dataFrame
        日次データを返す
    """
    currency = data["{}".format(nation)]
    currency = currency.astype(float)
    if(end == "no"):
        currency  = currency[begin:]
    else:
        currency = currency[begin:end]
    currency = pd.DataFrame(currency)
    currency = currency.T
    (currency.T).plot(figsize=(12, 8), title="USD / JPY")
    return currency