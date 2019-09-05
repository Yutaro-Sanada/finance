from statistics import mean
import pandas as pd


def five_days_moving_average(data, nation, begin, end):
    """
    5日移動平均を求める

    Parameters
    ----------
    data : pandas dataframe
        必要なデータ
    nation : chr
        欲しいデータの通貨名
    begin : int
        欲しいデータの開始日のindex
    end : int
        欲しいデータの最終日のindex + 1

    Return
    ------
    five_days : pandas DataFrame
        欲しい通貨の5日移動平均のデータ
    """
    currency = data["{}".format(nation)]
    currency = currency.T
    currency = currency.astype(float)
    if(end == "no"):
        partOfDate = currency[begin:]
    else:
        partOfDate = currency[begin:end]

    five_days = []
    for i in range(len((partOfDate.values).tolist()) - 4):
        five_days.append(mean((partOfDate.values).tolist()[i:i + 5]))

    date = list(partOfDate.index)
    five_days = pd.Series(five_days, index=date[4:])
    five_days = pd.DataFrame(five_days).T
    five_days.index = ["five days"]
    (five_days.T).plot(figsize=(12, 8), title="five days moving average")
    return five_days
