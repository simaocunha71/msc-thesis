def count_Occurrence(tup, lst):
    count = 0
    for ele in lst:
        count += tup.count(ele)
    return count

print(count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] )) # Outputs: 3

Explanation:
The function count_Occurrence takes in a tuple and a list as arguments. It initializes a count variable to 0. Then it iterates over each element in the list, adding the number of occurrences of that element in the tuple to the count variable. Finally, it returns the count variable.

Note that the tup.count(ele) method is used to count the number of occurrences of the element in the tuple. This method returns the number of times the element appears in the tuple.
"""

"""
