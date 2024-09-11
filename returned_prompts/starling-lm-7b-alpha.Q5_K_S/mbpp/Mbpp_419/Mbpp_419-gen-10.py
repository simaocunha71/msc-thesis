def round_and_sum(num_list):
    rounded_list = [round(i) for i in num_list]
    return sum(rounded_list) * len(rounded_list)

round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50])



"""
The above code defines a function called round_and_sum that takes in a list of numbers as an argument. Inside the function, a list comprehension is used to create a new list called rounded_list, in which each element is rounded to the nearest integer using the round() function. The sum() function is then used to calculate the total sum of the rounded_list, and the len() function is used to find the length of the rounded_list. Finally, the total sum is multiplied by the length of the list and returned as the result.

To test the function, the assert statement is used to check if the result of round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50]) is equal to 243. If the result is not equal to 243, an AssertionError will be raised, indicating that the function is not working correctly.
"""

def round_and_sum(num_list):
    rounded_list = [round(i) for i in num_list]
    return sum(rounded_list) * len(rounded_list)

round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50])


# Important
# In Python, the round() function is used to round a number to the nearest integer. This function takes one argument, which is the number to be rounded. The round() function returns the