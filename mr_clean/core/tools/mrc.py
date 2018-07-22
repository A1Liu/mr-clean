# -*- coding: utf-8 -*-
import pandas as pd
import mr_clean.core.functions.basics as basics
import mr_clean.core.functions.smart as sm
import mr_clean.core.stats.summary as stats

def clean(df,error_rate = 0):
    """ Superficially cleans data, i.e. changing simple things about formatting.
    Parameters:
    df - DataFrame
        DataFrame to clean
    error_rate - float {0 <= error_rate <= 1}, default 0
        Maximum amount of errors/inconsistencies caused explicitly by cleaning, expressed
        as a percentage of total dataframe rows (0 = 0%, .5 = 50%, etc.)
        Ex: na values from coercing a column of data to numeric
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
    ['Preview','Describe','Percentile Details',
     'Potential Outliers','Correlation Matrix']
    # use dtype stats to infer columns to change
    
    
    return df
    # TODO For future implementation