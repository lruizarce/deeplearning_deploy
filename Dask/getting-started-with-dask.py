import numpy as np
import pandas as pd
import dask.dataframe as dd
from dask.distributed import Client



def main():
    data_dict={
        "a": np.arange(5000),
        "b": np.random.rand(5000),
        "c": np.random.choice(["a", "b", "c"], 5000)
    }
    df = pd.DataFrame(data_dict)
    #print(df.head(10))
    
    # lazy dataframe we need to log dataframe to our mem
    ddf = dd.from_pandas(df, npartitions=10)
    #print(ddf)
    
    # call compute to log dataframe to mem
    #print(ddf.compute())
    
    
    # access partitions
    #print(ddf.partitions[3].compute())
    
    
    #sum_df = ddf.groupby("c").sum()
    #print(sum_df)
    
    
    #mean_df = ddf.groupby("c").mean() + 10
    #mean_df.visualize()
    
    @dask.delayed
    def increment(x: int): 
        return x + 1
    
    @dask.delayed
    def add(x, y):
        return x + y
    
    
    a = increment(1)
    b = increment(2)
    c = add(a,b)
    
    c.visualize()
    c.compute()
    print(c)
    
    
if __name__ == "__main__":
    client = Client()
    main()