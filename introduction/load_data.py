import requests
import pandas as pd
import  io

def load_data():
    """
    為替情報をダウンロードしてくる
    Parameter
    ---------
    None

    Return
    ------
    df : pandas DataFrame
        取得した為替情報
    """
    url = "https://www.mizuhobank.co.jp/market/csv/quote.csv"
    r = requests.get(url)
    df = pd.read_csv(io.BytesIO(r.content), sep=",", encoding="cp932")
    #読み込んだままだと扱いにくいからindexなどを修正し、indexを日付、columnsを通貨にする
    nameOfCurrency = list(df.iloc[1].values)
    nameOfCurrency = nameOfCurrency[1:]
    nameOfCurrency = nameOfCurrency[:31] + nameOfCurrency[32:]

    date = list(df.T.iloc[0].values)
    date = date[2:]

    df = df.drop(df.columns[[0, 32]], axis=1)
    df = df.T.drop(df.T.columns[[0, 1]], axis=1)
    df = df.T
    df.index = date
    df.columns = nameOfCurrency
    return df