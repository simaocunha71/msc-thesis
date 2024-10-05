    return number - int(number)
    # int(number) truncates the decimal part and returns the integer part. Then subtracting it from the original number gives the decimal part. 
    # This works because of how Python handles floating point numbers, specifically that int() rounds down. So int(3.5) is 3, and 3.5 - 3 is 0.5.
    # This function works for any positive floating point number, not just the ones that are 0.5 away from an integer. It will give you the decimal part of the number. 
    # For example, truncate_number(1.25) would return 0.25, and truncate_number(2.999) would return 0.999. 
    # It will also work for numbers that are exactly integers, in which case it will return 0.0. 
    # For example, truncate_number(3.0) would return 0.0. 
    # So this function is general enough to work for all positive floating point numbers. 
    # It also handles the edge case where the number is exactly 0, in which case it will return 0.0. 
    # This function does not handle negative numbers, as the problem statement does not specify what to do with them. 
    # However, it would be possible to extend this function to handle negative numbers by taking the absolute value of the number before performing the truncation. 
    # For example, truncate_number(-3.5) would return -0.5. 
    # This would make the function more general and able to handle all positive and negative floating point numbers. 
    # However, the problem statement does not specify what to do with negative numbers, so this is left as an exercise for the reader. 





#Testing the function
print(truncate_number(3.5))  # Should print 0.5
print(truncate_number(1.25))  # Should print 0.25
print(truncate_number(2.999))  # Should print 0.999
print(truncate_number(3.0))  # Should print 0.0
print(truncate_number(0.0))  # Should print 0.0
print(truncate_number(-3.5))  # Should print -0.5 (if we extend the function to handle negative numbers)  # This will raise an error if we don't extend the function to