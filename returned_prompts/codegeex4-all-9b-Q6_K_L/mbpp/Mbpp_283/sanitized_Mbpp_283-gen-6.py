def validate(num):
    # Convert the number to a string so we can iterate over its digits
    num_str = str(num)
    
    # Create a dictionary to store the frequency of each digit
    freq_dict = {}
    
    # Iterate over each digit in the string
    for digit in num_str:
        # Convert the digit back to an integer
        digit = int(digit)
        
        # If the digit is already in the dictionary, increment its count
        if digit in freq_dict:
            freq_dict[digit] += 1
        # Otherwise, add the digit to the dictionary with a count of 1
        else:
            freq_dict[digit] = 1
    
    # Iterate over each digit and its count in the dictionary
    for digit, count in freq_dict.items():
        # If the count is greater than the digit, return False
        if count > digit:
            return False
    
    # If we made it through the loop without returning False, return True
    return True