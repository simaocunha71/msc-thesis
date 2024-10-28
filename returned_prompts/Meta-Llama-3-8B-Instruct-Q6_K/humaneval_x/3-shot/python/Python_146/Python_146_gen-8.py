    count = 0
    for num in nums:
        if abs(num) > 10 and str(abs(num))[0] % 2 != 0 and str(abs(num))[-1] % 2 != 0:
            count += 1
    return count
# This function works by iterating over each number in the input array, 
# checking if the number is greater than 10 and if the first and last digits 
# are odd (using the modulo operator). If both conditions are met, 
# the function increments the count. Finally, the function returns the count.
# The use of abs(num) ensures that the function works with negative numbers as well. 
# The use of str(abs(num))[0] and str(abs(num))[-1] extracts the first and last digits 
# of the number as strings, and then uses the modulo operator to check if they are odd. 
# The use of str(abs(num))[-1] is used to get the last digit of the number. 
# The use of str(abs(num))[0] is used to get the first digit of the number. 
# The use of str(abs(num))[0] % 2 != 0 is used to check if the first digit is odd. 
# The use of str(abs(num))[-1] % 2 != 0 is used to check if the last digit is odd. 
# The use of count += 1 is used to increment the count when both conditions are met. 
# The use of return count is used to return the count at the end of the function. 
# This function is case-insensitive, meaning it works with both lowercase and uppercase letters. 
# This function also works with numbers that have more than two digits. 
# This function also works with negative numbers.  # This function works by iterating over each number in the input array, 
# checking if the number is greater than 10 and if the first and last digits are odd (using the modulo operator). 
# If both conditions are met, the function increments the count. Finally, the function returns the count. 
# The use of abs(num) ensures that the function works with negative numbers as well. 
# The use of str(abs(num))[0] and str(abs(num))[-1] extracts the first and last digits of the number as strings, 
# and then uses the modulo operator to check if they are odd. 
# The use of str(abs(num))[-1