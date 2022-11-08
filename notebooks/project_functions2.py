import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def pre_processing(x):

    filtered_Df = (
    pd.read_csv(x)
    .sort_values(by = ["date"], ascending = True)
    .dropna(axis=0)
    
    )
    return filtered_Df