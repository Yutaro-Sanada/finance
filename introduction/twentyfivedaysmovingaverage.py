from statistics import mean
import pandas as pd


def twenty_five_days_moving_average(data, nation, begin, end):
    """
    25日移動平均を求める

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
        欲しい通貨の25日移動平均のデータ
    """
    currency = data["{}".format(nation)]
    currency = currency.T
    currency = currency.astype(float)
    if(end == "no"):
        partOfDate = currency[begin:]
    else:
        partOfDate = currency[begin:end]

    twenty_five_days = []
    for i in range(len((partOfDate.values).tolist()) - 24):
        twenty_five_days.append(mean((partOfDate.values).tolist()[i:i + 25]))

    date = list(partOfDate.index)
    twenty_five_days = pd.Series(twenty_five_days, index=date[24:])
    twenty_five_days = pd.DataFrame(twenty_five_days).T
    twenty_five_days.index = ["twenty five days"]
    (twenty_five_days.T).plot(figsize=(12, 8), title="twenty five days moving average")
    return twenty_five_days
