# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import math
import warnings

warnings.resetwarnings()
warnings.simplefilter('ignore')

def main(df_data, column_name):
    df_data[column_name]=pd.to_datetime(df_data[column_name])
    
    #年月日でそれぞれ列を分ける
    
    df_date=pd.DataFrame()
    df_date[column_name+"_year"]=df_data[column_name].dt.year
    df_date[column_name+"_month"]=df_data[column_name].dt.month
    df_date[column_name+"_day"]=df_data[column_name].dt.day
    df_date[column_name+"_dayofweek"]=df_data[column_name].dt.dayofweek
    
    #月を周期関数で表現
    
    df_date[column_name+"_month_sin"]=float(0)
    df_date[column_name+"_month_cos"]=float(0)
    for index in df_date.index:
        df_date[column_name+"_month_sin"][index]=math.sin(2*3.14/12*df_date[column_name+"_month"][index])
        df_date[column_name+"_month_cos"][index]=math.cos(2*3.14/12*df_date[column_name+"_month"][index])
    
    df_date=df_date.drop(column_name+"_month", axis=1)
    
    #日を周期関数で表現(1-31日)
    
    df_date[column_name+"_day_sin"]=float(0)
    df_date[column_name+"_day_cos"]=float(0)
    for index in df_date.index:
        df_date[column_name+"_day_sin"][index]=math.sin(2*3.14/31*df_date[column_name+"_day"][index])
        df_date[column_name+"_day_cos"][index]=math.cos(2*3.14/31*df_date[column_name+"_day"][index])
    
    df_date=df_date.drop(column_name+"_day", axis=1)
    
    #曜日を周期関数で表現(日ー土:0-6)
    
    df_date[column_name+"_dayofweek_sin"]=float(0)
    df_date[column_name+"_dayofweek_cos"]=float(0)
    for index in df_date.index:
        df_date[column_name+"_dayofweek_sin"][index]=math.sin(2*3.14/7*df_date[column_name+"_dayofweek"][index])
        df_date[column_name+"_dayofweek_cos"][index]=math.cos(2*3.14/7*df_date[column_name+"_dayofweek"][index])
    
    df_date=df_date.drop(column_name+"_dayofweek", axis=1)
    
    df_data=pd.concat([df_data, df_date], axis=1)
    df_data=df_data.drop(column_name, axis=1)
    
    df_data.to_csv("date_encoded_data.csv")
    
    return df_data
    

if __name__=="__main__":
    
    df_data=pd.read_csv("Dataset\\marketing_campaign.csv", index_col=0, sep="\t")
    column_name="Dt_Customer"
    
    df_data=main(df_data, column_name)
    
