import pandas as pd
import plotly.figure_factory as ff
import statistics

df=pd.read_csv("Brands.csv")


RatingList=df["Avg Rating"].to_list

ratingMean=statistics.mean(RatingList)

print(ratingMean)




