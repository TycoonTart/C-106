import plotly_express as px
import csv
with open("coffe.csv") as f:
    df=csv.DictReader(f)
    fig=px.scatter(df,x="Coffee in ml",y="sleep in hours",color="week")
    fig.show()