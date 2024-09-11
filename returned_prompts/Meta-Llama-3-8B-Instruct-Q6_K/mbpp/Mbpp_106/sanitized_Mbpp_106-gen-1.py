def add_lists(lst, tup):
    return tup + tuple(lst)  # Convert list to tuple and concatenate.  # For Python 3.9 and above you can use this method
    #return tup + list(lst)  # Convert list to list and concatenate.  # For Python 3.9 and below you can use this method
    #return tup + (lst)  # This will raise TypeError: can only concatenate tuple (not "list") to tuple
    #return tup + lst  # This will also raise TypeError: can only concatenate tuple (not "list") to tuple