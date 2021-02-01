import pandas as pd

df = pd.read_csv("resources/cities.csv")
df.to_html("table.html", index=False, header=True)