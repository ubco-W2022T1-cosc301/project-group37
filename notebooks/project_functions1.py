import pandas as pd
import numpy as np

def load_and_process(fileName):
    df = pd.read_csv(fileName)
    loaderDataFrame = (df.copy()
                       .sort_values("date") 
                       .dropna(axis=0)
                 )
    
    return loaderDataFrame