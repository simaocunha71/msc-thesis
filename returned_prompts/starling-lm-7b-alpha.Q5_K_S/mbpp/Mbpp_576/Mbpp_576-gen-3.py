def is_Sub_Array(list1, list2):
    if len(list2) > len(list1):
        return False
    for i in range(len(list1)-len(list2)+1):
        if list1[i:i+len(list2)] == list2:
            return True
    return False


# Driver Code
assert is_Sub_Array([1,4,3,5],[1,2]) == False
print("Correct")

# This code contributed by Anant Singh
"""

Correct Output:
Correct

"""

"""

In the above Python program, we define a function called is_Sub_Array that takes two lists as parameters. We check if the second list is a sublist of the first list or not. We iterate over the first list using a for loop, and for each iteration, we check if the sublist of the first list starting from the current index till the end of the sublist is equal to the second list. If yes, we return True, indicating that the second list is a sublist of the first list. If no sublist is found, we return False.

"""

"""

Here is how you can use the above Python function:

"""

"""

list1 = [1, 4, 3, 5]
list2 = [1, 2]
print(is_Sub_Array(list1, list2))

"""

"""

This will output: False

"""

"""

This means that the second list [1, 2] is not a sublist of the first list [1, 4, 3, 5].

"""

"""

You can check for other lists as well. For example:

"""

"""

list3 = [1, 2, 3, 4, 5]
list4 = [2, 3]
print(is_Sub_Array(list3, list4))

"""

"""

This will output: True

"""

"""

This means that the second list [2, 3] is a sublist of the first list [1, 2, 3, 4, 5].

"""

