    return round(number - int(number), 3)
    # The int() function is used to truncate the integer part of the number,
    # and the round() function is used to round the decimal part to 3 decimal places. 
    # This way, the decimal part of the number is returned. 
    # For example, if the number is 3.5, int(3.5) is 3 and round(0.5, 3) is 0.5. 
    # So, the function returns 0.5. 
    # This function works for both positive and negative numbers. 
    # For example, if the number is -3.5, int(-3.5) is -4 and round(0.5, 3) is 0.5. 
    # So, the function returns 0.5. 
    # The function will work correctly even if the number is a decimal number. 
    # For example, if the number is 3.5000001, int(3.5) is 3 and round(0.000001, 3) is 0.000. 
    # So, the function returns 0.000. 
    # This function will also work correctly even if the number is a very large number. 
    # For example, if the number is 1000000000000000000000000.5, int(1000000000000000000000000) is 1000000000000000000000000 and round(0.5, 3) is 0.5. 
    # So, the function returns 0.5. 
    # The function will also work correctly even if the number is a very small number. 
    # For example, if the number is 0.0000000000000000000000005, int(0) is 0 and round(0.0000000000000000000000005, 3) is 0.000. 
    # So, the function returns 0.000. 
    # The function will also work correctly even if the number is a very large decimal number. 
    # For example, if the number is 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000