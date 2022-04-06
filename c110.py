import pandas as pd
import statistics
import random
import csv
import plotly.figure_factory as ff

df=pd.read_csv("newdata.csv")
data = df["average"].tolist()
poplution_mean = statistics.mean(data)

fig=ff.create_distplot([data],["average"],show_hist=False)
fig.show()