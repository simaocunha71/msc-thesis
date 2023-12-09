

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    
    # if the list is empty then return True or else perform an in-place
    # comparison of consecutive elements and return True based on the last
    # element. Note that we are using a variable named l to avoid shadowing
    # the builtin function name 'list'.
    # The below loop would work if all we wanted was to check whether or not
    # the list is empty:
    
    if len(l) == 0: return True
    
    else:
        
        l[0] < l[-1]: return False
        l[0] > l[-1]: return True
    pass
