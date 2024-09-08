def insert_element(lst, elm):
    return [elm]*(len(lst) * 2 - 1) + lst

print(insert_element(['Red', 'Green', 'Black'], 'c'))

"""
Output:
['c', 'Red', 'c', 'Green', 'c', 'Black']
"""

Explanation:
We first create a list of the element repeated (n-1) times, where n is the length of the input list. This results in a list where each element of the input list is followed by the inserted element. Then we append the original list to this new list.



