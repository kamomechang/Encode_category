# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder




def main(df_data):
    
    df_dtype=df_data.dtypes
    le=LabelEncoder()
    df_encode_table=pd.DataFrame()
    
    for column in df_data.columns:
        if df_dtype[column]=="object":
            label_encoder=le.fit(df_data[column])
            df_data[column]=le.transform(df_data[column])
            df=pd.DataFrame(label_encoder.classes_)
            df_encode_table=pd.concat([df_encode_table, df], axis=1)
    df_data.to_csv("le_encoded_data.csv")
    df_encode_table.to_csv("le_table.csv")
    
    return df_data
             
if __name__=="__main__":
    
    df_data=pd.read_csv("Dataset\\marketing_campaign.csv", index_col=0, sep="\t")
    
    df_data=main(df_data)
    
