"""
def sample_nam(lis):
    lis=[i for i in lis if i[0].isupper()]
    return sum(len(i) for i in lis)
"""

# The above code can be simplified by using the built-in function filter() and sum() as follows:

def sample_nam(lis):
    return sum(len(i) for i in filter(lambda x: x[0].isupper(), lis))

# Test the function
assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']) == 16

"""
The function sample_nam() filters the names in the list lis to keep only those names that start with an uppercase letter. Then, for each of these names, it calculates the length of the name and sums these lengths. Finally, it returns the total length of all the names that start with an uppercase letter.
"""

# Here's a step-by-step explanation of the code:

# 1. The function sample_nam() takes a list of names as input.
# 2. It uses the filter() function to filter the names in the list lis, keeping only those names that start with an uppercase letter. The lambda function is used as the filtering criterion.
# 3. The filter() function returns an iterator that produces the names that start with an uppercase letter.
# 4. The sum() function is used to sum the lengths of all these names. It takes a generator expression as input, which calculates the length of each name in the filtered list.
# 5. The result is the total length of all the names that start with an uppercase letter.
# 6. The assert statement is used to test the function and ensure that it returns the correct result for the given example.

# This code can be used to sum the length of the names of a given list of names after removing the names that start with a lowercase letter.

# Note: The isupper() method is a string method that returns True if the first character of the string is uppercase, otherwise False. The lambda function is an anonymous function that takes an item from the list and checks if the first character of the item is uppercase.

