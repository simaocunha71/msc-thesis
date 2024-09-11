"""
The problem is to calculate the average of each tuple in a tuple of tuples.

To solve this problem, first initialize an empty list called `result`. Then iterate over the input tuple using a `for` loop. For each tuple, initialize a variable called `sum` to 0. Then use a second `for` loop to iterate over each element in the tuple and add it to the `sum` variable. After the second loop, append the `sum` variable divided by the number of elements in the tuple to the `result` list.

Here is the Python code to solve this problem:
"""

def average_tuple(t):
    result = []
    for tup in t:
        sum = 0
        for num in tup:
            sum += num
        result.append(sum / len(tup))
    return result

# Test the function
assert average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4)))==[30.5, 34.25, 27.0, 23.25]







# Python 3 program to find the average of all elements in a tuple
# of tuples

# Function to find the average of all elements in a tuple
# of tuples
def average_tuple(t):

    result = [] # Empty list to store the average of each tuple

    # Iterate over the input tuple
    for tup in t:

        sum = 0 # Initialize the sum to 0

        # Iterate over each element in the tuple
        for num in tup:

            # Add each element to the sum
            sum += num

        # Append the sum divided by the number of elements in the tuple
        # to the result list
        result.append(sum / len(tup))

    return result

# Driver Code
t = ((10, 10, 10, 12), (30, 45, 56, 45), (81,