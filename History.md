# Changelog


#### Version 0.0.5

* Re-ordered changelog to have most recent version on top.
* Changed functionality of summarize
    * Summarize function was doing too much: moved some of the extra stuff to a new diagnose function
    * It now no longer gets df.info() information or datatype information
    * The parameter preview_rows now specifies the amount of rows to display in the preview. The format has changed to the following, where *n* represents the minimum of the value specified by preview_rows and the total amount of rows in the DataFrame:
        * floor(n/4) header rows
        * n - 2 * floor(n/4) rows sampled from the middle of the DataFrame (excludes header and tail rows)
        * floor(n/4) tail rows
* Added diagnose function
    * Subset of functionality originally in 'summarize' function.
    * Preview of dataset, df.info(), df data types, and potential outliers
    * Preview of dataset works exactly how preview works in new summarize function

#### Version 0.0.4
* Added documentation for methods.  
* Added corr_matrix function that expands on the functionality of pd.DataFrame.corr by adding support for categorical and boolean data.
* Added flexibility to the summarize function.
    * It now outputs describe for both numeric and non-numeric data.
    * It also now outputs a less noisy version of the outlier DataFrame, while maintaining the same amount of information
    * Finally, it now also supports outputting to a folder, and printing the entire DataFrame outputs as .csv files.

#### Version 0.0.3
Changed package structure again, and added more statistics methods.

#### Version 0.0.2
Changed the package structure to allow for easier development in future.
