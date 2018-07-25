# -*- coding: utf-8 -*-

# Utility function get longest common substrings from a list of substrings

import pandas as pd
from anytree import Node

def substr_list(str_list,length = -1,repeats = True):
    """ Gets a list of common substrings, ordered by length
    Parameters:
    str_list - list of strings
        List of strings to find the common substrings of
    length - int, default -1
        Lower limit for the length of the strings in the list. All strings with length
        equal to or less than the limit are returned. If set to -1, then all will be returned
    repeats - bool, default True
        Whether or not elements in the list can be substrings of longer elements in the list. 
        
        WARNING:
        If set to false, runtime of this function could increase substantially. Checking for 
        repeats is currently on the order of O(n^2*s) operation, where 'n' is the amount of 
        elements and 's' is the average length of the strings in the list.
    
    Ex:
        substr_list(['asdf','dfwed','_as'])
        output = ['df','as','a','s','d','f','w','e','_']
    
    Ex: 
        substr_list(['asdf','dfwed','_as'],length = 2)
        output = ['df','as']
    Ex:
        substr_list(['asdf','dfwed','_as'],repeats = False)
        output = ['df','as','w','e','_']
    """
    
    str_list = pd.Series(str_list)
    
    # Documentation for tree structure https://pypi.org/project/anytree/
    
    # Method: Suffix Tree https://en.wikipedia.org/wiki/Generalized_suffix_tree
    
    # Description: https://en.wikipedia.org/wiki/Longest_common_substring_problem
    
    # TODO Lol the entire thing
    
    # Plan
    
    # Get suffix tree
    
    # Get list of common substrings
    
    # Filter by length if necessary
    
    # Filter by repeats if necessary
    
    
    return substr_list

def suffix_tree(str_list):
    pass

def substr_unfiltered(suf_tree):
    pass

def sort_by_length(str_list):
    pass

def filter_by_length(str_list):
    pass

def filter_by_repetition(str_list):
    pass