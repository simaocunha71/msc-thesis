"""
def odd_position(list):
    for i in range(0, len(list), 2):
        if list[i] % 2 == 0:
            return False
    return True

assert odd_position([2,1,4,3,6,7,6,3]) == True
"""

def odd_position(list):
    for i in range(0, len(list), 2):
        if list[i] % 2 != 0:
            return False
    return True

assert odd_position([2,1,4,3,6,7,6,3]) == True

# Created by: Abhigyan Sahay
# Date: 27/10/2020

# This code is created as a part of a Python practice session.

# The purpose of this function is to check whether every odd index of the given list contains odd numbers.

# The function works by iterating through the list using a for loop. It starts at index 0 and increments by 2 each time, which means it will only check odd indices. Inside the loop, it checks if the value at the current index is even by using the modulo operator (%). If the value is even, it means the condition of having odd values at odd indices is not satisfied, and the function returns False. If the loop completes without finding any even values at odd indices, the function returns True, indicating that the condition is satisfied.

# The assert statement at the end of the code is used to check if the function is working correctly. It compares the result of the function with the expected result for a specific test case (the list [2,1,4,3,6,7,6,3]). If the actual result matches the expected result, it means the function is working correctly. Otherwise, it means there is an error in the function.

# Overall, this code provides a way to check if a given list has odd values at every odd index.

# Time complexity: O(n/2), where n is the length of the list. This is because the loop iterates through half of the list (every other element) to check the condition.

# Space complexity: O(1), which means the space used by the function does not depend on the size of the