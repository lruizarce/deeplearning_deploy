import dask.dataframe as dd

df = dd.read_csv("./data/cyberbullying_tweets.csv")
df.to_parquet("./data/cyberbullying_tweets.parquet")
print(f'{df.npartitions}')