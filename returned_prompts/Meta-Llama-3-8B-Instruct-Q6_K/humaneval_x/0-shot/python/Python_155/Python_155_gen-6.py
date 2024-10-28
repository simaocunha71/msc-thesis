    # convert the input integer to a string to easily iterate over each digit
    num_str = str(abs(num))  # take the absolute value to handle negative numbers
    
    even_count = 0
    odd_count = 0
    
    # iterate over each digit in the string
    for digit in num_str:
        # convert the digit back to an integer
        digit_int = int(digit)
        
        # check if the digit is even or odd
        if digit_int % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    return even_count, odd_count
    # return a tuple with the even and odd counts
    # return (even_count, odd_count) # if you want a tuple

# test the function
print(even_odd_count(-12))  # should return (1, 1)
print(even_odd_count(123))  # should return (1, 2)  # example output: (1, 2)  # should return (1, 2)  # example output: (1, 2)  # should return (1, 2)  # example output: (1, 2)  # should return (1, 2)  # example output: (1, 2)  # should return (1, 2)  # should return (1, 2)  # should return (1, 2)  # should return (1, 2)  # should return (1, 2)  # should return (1, 2)  # should return (1, 2)  # should return (1, 2)  # should return (1, 2)  # should return (1, 2)  # should return (1, 2)  # should return (1, 2)  # should return (1, 2)  # should return (1, 2)  # should return (1, 2)  # should return (1, 2)  # should return (1, 2)  # should return (1, 2)  # should return (1, 2)  # should return (1, 2)  # should return (1, 2)  # should return (1, 2)  # should return (1, 2)  # should return (1