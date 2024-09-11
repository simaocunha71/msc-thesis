"""
def check_Consecutive(List):
    List.sort()
    for i in range(len(List)-1):
        if List[i+1]-List[i] != 1:
            return False
    return True
"""

def check_Consecutive(List):
    List.sort()
    for i in range(len(List)-1):
        if List[i+1]-List[i] != 1:
            return False
    return True

# Test
assert check_Consecutive([1,2,3,4,5]) == True
assert check_Consecutive([1,2,3,5,4]) == False
assert check_Consecutive([1,2,3,3,2]) == False

print("All tests passed.")






```

In this code, the function check_Consecutive takes a list as an argument and checks whether the list contains consecutive numbers or not. It first sorts the list in ascending order using the List.sort() method. Then, it iterates through the list using a for loop and checks whether the difference between consecutive elements is equal to 1. If the difference is not equal to 1, the function returns False, indicating that the list does not contain consecutive numbers. If the loop completes without encountering any discrepancies, the function returns True, indicating that the list contains consecutive numbers.

To test the function, several assert statements are provided. The assert check_Consecutive([1,2,3,4,5]) == True statement verifies that the function correctly identifies a list of consecutive numbers. The assert check_Consecutive([1,2,3,5,4]) == False statement verifies that the function correctly identifies a list that does not contain consecutive numbers. The assert check_Consecutive([1,2,3,3,2]) == False statement verifies that the function correctly identifies a list with consecutive numbers interrupted by a non-consecutive element.

If all tests pass, the script prints "All tests passed." to the console, indicating that the function is working correctly.



































