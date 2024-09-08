def remove_kth_element(lst,k):
    return lst[:k] + lst[k+1:]

print(remove_kth_element([1,1,2,3,4,4,5,1],3))

"""
Explanation:
The function remove_kth_element takes a list and an integer k as arguments.
It returns a new list that consists of the elements of the original list except the k'th one.
This is done by using Python's list slicing feature. The [:k] gets all elements from the start of the list up to, but not including, the k'th element, and [k+1:] gets all elements from the k'th element to the end of the list.
The + operator is used to join these two parts together.
"""

