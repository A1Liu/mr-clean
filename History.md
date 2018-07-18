# Changelog

#### Version 0.0.2
Changed the package structure to allow for easier development in future.

#### Version 0.0.3
Changed package structure again, and added more statistics methods.

#### Version 0.0.4
* Added documentation for methods.  
* Added corr_matrix function that expands on the functionality of pd.DataFrame.corr by adding support for categorical and boolean data.
* Added flexibility to the summarize function.
    * It now outputs describe for both numeric and non-numeric data.
    * It also now outputs a less noisy version of the outlier DataFrame, while maintaining the same amount of information
    * Finally, it now also supports outputting to a folder, and printing the entire DataFrame outputs as .csv files.
