import dask.dataframe as dd

df = dd.read_csv("./data/cyberbullying_tweets.csv")
print(df.columns)