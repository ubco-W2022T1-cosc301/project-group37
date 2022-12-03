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

def MovingAverage(df, stock):
    df['MovingAverage2'] = df['close'].rolling(60).mean()
    df['MovingAverage4'] = df['close'].rolling(120).mean()
    df['close'].plot(figsize = (18,9))
    df['MovingAverage2'].plot()
    df['MovingAverage4'].plot()
    plt.title('Moving Average of '+stock+' stocks')
    plt.legend()
    plt.xlabel('Date')
    plt.ylabel('Stock Value (S)')
    
    