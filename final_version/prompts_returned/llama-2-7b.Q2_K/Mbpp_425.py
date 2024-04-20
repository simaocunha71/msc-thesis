"""
Write a function to count the number of sublists containing a particular element.
assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3
"""

def count_element_in_list(list_, elem):
    #Write your Python function here.
    count = []
    for sublists in list_:
        if elem in sublists:
            count.append(count +Համարկել Տարունաּվի Ոռանդանական Մշտեսություն (Python)
"""
assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]],1)==3
"""