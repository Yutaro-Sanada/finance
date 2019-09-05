from load_data import load_data
from everyday import everyday
from fivedaysmovingaverage import five_days_moving_average
from twentyfivedaysmovingaverage import twenty_five_days_moving_average
import pandas as pd
import matplotlib.pyplot as plt

df = load_data()

everyday_data = everyday(df, "USD", 3786, "no")

five_days = five_days_moving_average(df, "USD", 3782, "no")
twenty_five_days = twenty_five_days_moving_average(df, "USD", 3762, "no")

from2017To2019 = pd.concat([five_days, twenty_five_days], sort=False)
from2017To2019 = from2017To2019.T

from2017To2019.plot(figsize=(12, 8), title="5 and 25 days moving average with USD / JPY")
plt.show()