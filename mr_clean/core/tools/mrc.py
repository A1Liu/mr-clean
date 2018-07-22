# -*- coding: utf-8 -*-
import pandas as pd
import mr_clean.core.functions.basics as basics
from mr_clean.core.functions.scrub import smart_scrub
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
    
    # Remove extra whitespace
    for col_name in df.select_dtypes(include = 'object').columns:
        df[col_name] = basics.col_strip(df,col_name)
        print("Stripped extra whitespace from '{}'".format(col_name))
        smart_coerce(df,col_name)
        new_dtype = smart_coerce(df,col_name)
        if new_dtype is not None:
            print("Coerced '{}' to datatype '{}'".format(col_name, new_dtype))

    # Scrub columns
    for col_name in df.select_dtypes(include = 'object').columns:
        scrubf, scrubb = smart_scrub(df,col_name,1-error_rate)
        if scrubf is not None or scrubb is not None:
            print("Scrubbed '{}' from the front and '{}' from the back of column '{}'" \
                  .format(scrubf,scrubb,col_name))
        else:
            continue
        new_dtype = smart_coerce(df,col_name)
        if new_dtype is not None:
            print("Coerced '{}' to datatype '{}'".format(col_name, new_dtype))
    
    # Change format of entries to numeric if possible
    dtype_stats = stats.dtypes_summary(df)
    ['rows_numerical','rows_string','rows_date_time','category_count','largest_category','rows_na','rows_total']
    
    # use dtype stats to infer columns to change
    
    
    return df
    # TODO For future implementation