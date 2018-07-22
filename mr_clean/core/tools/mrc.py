# -*- coding: utf-8 -*-
import pandas as pd
import mr_clean.core.functions.basics as basics
import mr_clean.core.functions.smart as sm
import mr_clean.core.stats.summary as stats
import mr_clean.core.stats.regression as reg




def clean(df,error_rate = 0):
    """
    """
    df = df.copy()
    
    # Change colnames
    basics.clean_colnames(df)
    print('Changed colnames to {}'.format(df.columns))
    
    col_types = basics.col_dtypes(df)
    
    # Remove extra whitespace
    for col_name in df.columns:
        df[col_name] = basics.col_strip(df,col_name)
    
    # Scrub columns
    for col_name in df.columns:
        if col_types[col_name] == 'object':
            scrubf, scrubb = sm.smart_scrub(df,col_name,1-error_rate)
            if scrubf is not None or scrubb is not None:
                print("Scrubbed '{}' from the front and '{}' from the back of column '{}'" \
                      .format(scrubf,scrubb,col_name))
    
    # Change format of entries to numeric if possible
    dtype_stats = stats.dtypes_summary(df)
    # use dtype stats to infer columns to change
    
    
    return df
    # TODO For future implementation



# validates input
def validate(df,coerce_numeric,coerce_dt,coerce_categorical): 
    assert type(df) is pd.DataFrame
    column_dict = {}
    for element in coerce_numeric + coerce_dt + coerce_categorical: # these lists must be mutually exclusive
        assert type(element) is str
        assert not element in column_dict
        column_dict[element] = True
