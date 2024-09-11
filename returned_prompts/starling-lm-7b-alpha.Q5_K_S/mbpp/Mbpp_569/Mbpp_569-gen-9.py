"""
def sort_sublists(sublists):
    for i in range(len(sublists)):
        sublists[i].sort()
    return sublists
"""

def sort_sublists(sublists):
    # Using list comprehension and map() function
    return [sorted(sublist) for sublist in sublists]

# Testing the function
assert sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']])==[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
print("All Test cases Passed")














"""
In Python, the built-in function sorted() is used to sort the list of strings. The sorted() function returns a new list that is sorted according to the default ascending order. The default sort order is numeric and the list is sorted as a whole.
The syntax of sorted() function is as follows:

sorted(list, key=None, reverse=False)

In the above function,

list: is the list that is to be sorted.
key: is a function that takes an item from the list and returns a key to use for sorting purposes. It is optional.
reverse: is a boolean value that when set to True, the list is sorted in descending order. It is optional.

The above function can be used in the following way:

sorted(list)

For example, consider the following list:

list = [2, 5, 3, 6, 1, 4]

To sort the above list in ascending order, we can use the sorted() function as follows:

sorted_list = sorted(list)

After executing the above code, the sorted_list will be:

sorted_list = [1, 2, 3, 4, 5, 6]

Now, let us use the above function to sort each sublist of strings in a given list of lists:

def sort_sublists(sublists):
    for i in range(len(sublists)):
        sublists[i].sort()
    return sublists

In