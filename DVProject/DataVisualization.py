import pandas as pd
import plotly.express as px
import csv

df = pd.read_csv("Data.csv")
student_df=df.loc[df['student_id']=='TRL_xs1']
print(df.groupby("level")["attempt"].mean())

fig = px.scatter(df,x="level",y="attempt",)

fig.show()