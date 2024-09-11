"""
Here is a function that checks whether a given list contains the given sublist or not:

def is_sublist(list_a, sublist):
    # Iterate through the list and check
    # whether sublist is present or not
    for i in range(len(list_a)-len(sublist)+1):
        if list_a[i:i+len(sublist)] == sublist:
            return True
    return False

To check the function, we can use the following assertion:

assert is_sublist([2,4,3,5,7],[3,7])==False

The function iterates through the list and checks whether the sublist is present or not. If the sublist is found, the function returns True. If the sublist is not found, the function returns False.
"""

# Python3 program to check if a list
# contains a sublist or not

# Function to check if a list
# contains a sublist or not
def isSublist(list_a, sublist):

    # Iterate through the list and check
    # whether sublist is present or not
    for i in range(len(list_a)-len(sublist)+1):
        if list_a[i:i+len(sublist)] == sublist:
            return True
    return False

# Driver code

list_a = [2,4,3,5,7]
sublist = [3,7]

# Check if list contains sublist
if isSublist(list_a, sublist):
    print("Yes")
else:
    print("No")





"""
In this code, we define a function called isSublist that takes in two parameters: list_a, which is the main list, and sublist, which is the sublist we want to check for. The function iterates through the list_a using a for loop and checks whether the sublist is present in the list_a using the slicing technique. If the sublist is found, the function returns True. If the sublist is not found, the function returns False.

To test the function, we define a main list called list_a and a sublist called sublist. We then use the