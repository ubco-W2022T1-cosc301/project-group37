#importing libraries
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE
from sklearn.linear_model import RidgeCV, LassoCV, Ridge, Lasso
from datetime import datetime

#We create the function that takes into account changements made by Task1 and Task2

def load_and_process(path_to_csv_file):
    # Method Chain 1 (Load data and deal with not correlated data)
    df1 = (
        pd.read_csv(path_to_csv_file)
    )
    cor = df1.corr()
    irr_cor_target = abs(cor["Total Revenue"])#Selecting highly uncorrelated features
    irrelevant_features = irr_cor_target[irr_cor_target<0.7]
    irrelevant_features_in_list=irrelevant_features.index.tolist()
    irrelevant_features_in_list.remove('For Year') #we can need the year even if there are no correlation with this variable
    
    # Method Chain 2 (Drop useless columns, drop outlier in year data)
    df2 = (
        df1.copy().drop(irrelevant_features_in_list, axis=1)
        .dropna(axis=0)
    )
    df2 = df2[df2['For Year'].between(2011, 2017)]
    
    # Method Chain 3 : dropping all the dates except 31 decembers, taking away the uncorrelated features
    df3 = (
        df2.copy().drop('Net Income-Cont. Operations', axis=1)
    )

    periods = np.array(df3['Period Ending'])
    datetimeforperiods=[]
    for period in periods:
        date_time_obj = datetime.strptime(period, '%Y-%m-%d')
        datetimeforperiods.append(date_time_obj)
    dates = np.array(datetimeforperiods)
    df3['PeriodEndingInDate'] = dates.tolist()
    
    df_cleaned_dec2012 = df3.copy()[df3['PeriodEndingInDate']==('2012-12-31 00:00:00')]
    df_cleaned_dec2013 = df3.copy()[df3['PeriodEndingInDate']==('2013-12-31 00:00:00')]
    df_cleaned_dec2014 = df3.copy()[df3['PeriodEndingInDate']==('2014-12-31 00:00:00')]
    df_cleaned_dec2015 = df3.copy()[df3['PeriodEndingInDate']==('2015-12-31 00:00:00')]
    df_cleaned_dec2012 = df_cleaned_dec2012.copy()[df_cleaned_dec2012['For Year']==(2012)]
    df_cleaned_dec2013 = df_cleaned_dec2013.copy()[df_cleaned_dec2013['For Year']==(2013)]
    df_cleaned_dec2014 = df_cleaned_dec2014.copy()[df_cleaned_dec2014['For Year']==(2014)]
    df_cleaned_dec2015 = df_cleaned_dec2015.copy()[df_cleaned_dec2015['For Year']==(2015)]
    
    df4 = (
        pd.concat([df_cleaned_dec2012, df_cleaned_dec2013,df_cleaned_dec2014,df_cleaned_dec2015], axis=0)
        .drop('Period Ending', axis=1)
        .drop('PeriodEndingInDate', axis=1)
        #.drop('Ticker Symbol', axis=1)
    )    
    # Make sure to return the latest dataframe
    return df4