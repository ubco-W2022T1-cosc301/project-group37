import pandas as pd
import numpy as np

def load_and_process(fileName):
    df = pd.read_csv(fileName)
    loaderDataFrame = (df.copy()
                       .sort_values("date") 
                       .dropna(axis=0)
                 )
    loaderDataFrame['reported_year'] = pd.to_datetime(loaderDataFrame['date']).dt.year
    loaderDataFrame['reported_month'] = pd.to_datetime(loaderDataFrame['date']).dt.month
    
    return loaderDataFrame