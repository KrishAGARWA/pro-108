import pandas as pd
import plotly.figure_factory as px
import csv

df=pd.read_csv("mobile.csv")
fig=px.create_distplot([df["Avg Rating"].tolist()],["mobile average rating"],show_hist=False)
fig.show()
