"""
To achieve this we can use slicing on each string to get the last character.
We can use a for loop to iterate over the tuple and append each character to a list.
Finally we return the list. Here's an example of how you can implement this:
"""
def extract_rear(tup):
    result = []
    for i in tup:
        result.append(i[-1])
    return result
# Here's a test of the function:
print(extract_rear(('Mers', 'for', 'Vers'))) # Output: ['s', 'r', 's']
























"""
In the above code, the `extract_rear` function takes in a tuple as an argument. It initializes an empty list called `result` to store the extracted rear index characters.

Next, it uses a for loop to iterate over each element in the tuple. For each element, it uses slicing `i[-1]` to get the last character and appends it to the `result` list.

Finally, the function returns the `result` list containing the rear index characters of each string in the tuple.

To test the function, the code prints the result of calling `extract_rear` with the tuple `('Mers', 'for', 'Vers')`. The expected output is `['s', 'r', 's']`, which matches the actual output.
"""

"""
Here's an alternate implementation using list comprehension:
"""
def extract_rear(tup):
    return [i[-1] for i in tup]
# Here's a test of the function:
print(extract_rear(('Mers', 'for', 'Vers'))) # Output: ['s', 'r', 's']


















"""
In the above code, the `extract_rear` function takes in a tuple as an argument. It uses list comprehension to create a new list containing the rear index characters of each string in the tuple.

The list comprehension `[i[-1] for i in tup]` iterates over each element `i