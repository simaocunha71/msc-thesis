def min_of_three(a, b, c):
    return min(a, b, c)  # Python's built-in min function can take multiple arguments
    # return min(a if a < b else b, c if c < a else b) # Alternative solution using if-else condition
    # return min(a, min(b, c)) # Alternative solution using min function again
    # return a if a < b and a < c else (b if b < c else c) # Alternative solution using if-else condition
    # return min([a, b, c]) # Alternative solution using list and min function
    # return a # This will return the first number if all numbers are equal, so it might not be correct for all cases
    # return c # This will return the last number if all numbers are equal, so it might not be correct for all cases
    # return b # This will return the second number if all numbers are equal, so it might not be correct for all cases
    # return min(a,b,c) # This will return the smallest number, it might not be correct for all cases
    # return min(a) # This will return the smallest number, it might not be correct for all cases
    # return min(b) # This will return the smallest number, it might not be correct for all cases
    # return min(c) # This will return the smallest number, it might not be correct for all cases
    # return min(min(a,b),c) # This will return the smallest number, it might not be correct for all cases
    # return min(min(b,c),a) # This will return the smallest number, it might not be correct for all cases
    # return min(min(a,c),b) # This will return the smallest number, it might not be correct for all cases
    # return min(min(a,b),min(c,d)) # This will return the smallest number, it might not be correct for all cases
    # return min(min(b,c),min(a,d)) # This will return the smallest number, it might not be correct for all cases
    # return min(min(a,c),min(b,d)) # This will return the smallest number, it might not be correct for all cases
    # return min(min(a,b),min(c,d)) # This will return the smallest number, it might not be correct for all cases
    # return min(min(b,c),min