# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

def main(df_data):
    
    
    df_data=pd.get_dummies(df_data, dummy_na=True, drop_first=True)
    df_data.to_csv("ohe_encoded_data.csv")
    return df_data
             
if __name__=="__main__":
    
    df_data=pd.read_csv("Dataset\\marketing_campaign.csv", index_col=0, sep="\t")
    df_data=main(df_data)