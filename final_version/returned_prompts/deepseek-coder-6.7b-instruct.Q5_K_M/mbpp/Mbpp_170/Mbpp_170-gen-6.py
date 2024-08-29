"""
This function will find the sum of the numbers in a list within a range specified by two indices. 
The function takes in a list of numbers and two indices as input.
The function will then use a for loop to iterate through the list from the start index to the end index (inclusive).
It will then add all of the numbers in this range to a sum variable.
Finally, it will return the sum variable.
"""

def sum_range_list(numbers, start_index, end_index):
    sum = 0
    for i in range(start_index, end_index+1):
        sum += numbers[i]
    return sum
"""
Testing the function with the given question:
"""
print(sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10)) # Expected output: 29

# End of code

"""
This solution is efficient as it runs in O(n) time complexity where n is the size of the list. 
It iterates through the list once to add up the numbers in the specified range.
"""
<jupyter_output>
29
<jupyter_text>
Question 4
<jupyter_code>
"""
