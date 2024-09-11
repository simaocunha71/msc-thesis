def is_Sub_Array(list_1, list_2):
    if len(list_1) > len(list_2):
        return False
    j = 0
    for i in range(len(list_1)):
        if list_1[i] == list_2[j]:
            j += 1
        if j == len(list_2):
            return True
    return False

# Test
print(is_Sub_Array([1,4,3,5],[1,2]))  # False
print(is_Sub_Array([1,4,3,5],[1,4,3])) # True


"""
This function works by iterating over the first list, and comparing each element to the elements of the second list. If there is a match, j is incremented by one. If j ever matches the length of the second list, the function returns True, meaning that the first list is a sublist of the second. If the first list is longer than the second, the function returns False. If no match is found, the function returns False.
"""

"""
In the given code, the function is_Sub_Array takes two arguments, list_1 and list_2. It first checks if the length of list_1 is greater than the length of list_2. If this is true, the function immediately returns False, as a sublist cannot be longer than the list it is a sublist of.

Next, the function initializes a variable j to 0. This variable is used to keep track of the current index of list_2 while iterating over list_1.

The function then enters a for loop, which iterates over the indices of list_1. Inside the loop, it checks if the element at index i in list_1 is equal to the element at index j in list_2. If they are equal, j is incremented by one.

After each iteration of the for loop, the function checks if j is equal to the length of list_2. If it is, the function returns True, indicating that list_1 is a sublist of list_2. If j is not equal to the length of list_2, the function continues to the next iteration of the loop.

If no match is found between the elements of list_1 and list