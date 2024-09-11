"""
Here is a way to do it:

def max_sum_list(list_of_lists):
    max_sum = 0
    max_sum_list = []
    for sublist in list_of_lists:
        curr_sum = sum(sublist)
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_sum_list = sublist
    return max_sum_list

The function above takes a list of lists as an argument and iterates over each sublist. It calculates the sum of each sublist and keeps track of the highest sum. When the sum of a sublist is higher than the current max sum, it updates the max_sum and max_sum_list variables. Finally, it returns the list whose sum is the highest."""

# Python Program to Find the List with Maximum Sum in a List of Lists
def max_sum_list(list_of_lists):
    max_sum = 0
    max_sum_list = []
    for sublist in list_of_lists:
        curr_sum = sum(sublist)
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_sum_list = sublist
    return max_sum_list

# Driver Code
list_of_lists = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
print(max_sum_list(list_of_lists))  # prints [10, 11, 12]

# This code is Contributed by Anant Agarwal.

"""
This program defines a function called max_sum_list that takes a list of lists as an argument. It initializes two variables, max_sum and max_sum_list, to keep track of the highest sum and the corresponding sublist, respectively.

The function then iterates over each sublist in the list_of_lists. For each sublist, it calculates the sum of its elements using the sum() function and stores it in the curr_sum variable. If the curr_sum is higher than the current max_sum, it updates the max_sum