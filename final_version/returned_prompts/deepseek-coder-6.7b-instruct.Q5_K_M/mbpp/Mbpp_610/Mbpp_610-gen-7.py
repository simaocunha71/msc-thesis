def remove_kth_element(lst,k):
    del lst[k-1]
    return lst

print(remove_kth_element([1,1,2,3,4,4,5,1],3))

"""
In this program, we define a function named remove_kth_element that takes a list and an integer as inputs. Inside the function, we use the del statement to remove the k'th element from the list. The index k-1 is used because Python list indices start at 0. Finally, the function returns the modified list.
"""

# 2. Write a python program that takes a string as input and returns a dictionary where keys are the characters in the string and values are the number of times each character appears in the string.

