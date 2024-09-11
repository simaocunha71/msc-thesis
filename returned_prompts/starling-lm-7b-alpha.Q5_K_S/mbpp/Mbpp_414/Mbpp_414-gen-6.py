from collections import Counter

def overlapping(list_1, list_2):
    c = Counter(list_1)
    return any(i in c for i in list_2)



# Driver program
print(overlapping([1, 2, 3, 4, 5], [6, 7, 8, 9]))




"""
This is the solution to the above problem. We are using Counter from collections module to count the occurrence of all items in a given list and then we are checking if any of the items in the other list is present in the first list or not using any() function of Python.
"""








"""
In this program, we are using Counter class of the collections module to get a dictionary with keys as the elements of the list and the values as the count of the number of occurrences of the element in the list.

After that, we are using any() function to check if any element from the second list exists in the first list or not. The any() function returns True if any element in the iterable is true.

In this case, if any element from the second list exists in the first list, the any() function will return True, else it will return False.
"""


"""
The above program can be used to check if any element in a list exists in another list or not. It can also be used to check if the intersection of two lists is empty or not.
"""








"""
The time complexity of this program is O(n) as we are iterating over the first list to create a dictionary of the elements and their counts.

The space complexity of this program is O(n) as we are creating a dictionary to store the counts of the elements of the list.
"""


"""
In this program, we are using Counter class of the collections module to count the occurrence of all items in a given list and then we are checking if any of the items in the other list is present in the first list or not using any() function of Python.

The any() function returns True if any element in the iterable is true. In this case, if any element from the second list exists in the first list, the any() function will return True, else