def consecutive_duplicates(lst):
    """
    Remove consecutive duplicates of a given list
    """
    new_lst = []
    for i in range(len(lst)):
        if i == 0 or lst[i] != lst[i-1]:
            new_lst.append(lst[i])
    return new_lst

# Unit Test
def test():
    assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
    print("All Tests Passed.")

test()







"""
The function works by initializing a new list called new_lst. It then iterates through the original list by using a for loop and the range function. Inside the loop, it checks if the current index is 0 (the first element of the list) or if the current element is not equal to the previous element. If either of these conditions is true, it means that the element is not a consecutive duplicate, so it is appended to the new_lst. Finally, the function returns the new_lst, which contains the original list with consecutive duplicates removed.

The unit test function test() is used to verify that the function is working correctly. It calls the consecutive_duplicates function with a sample input and asserts that the output matches the expected result. If all tests pass, it prints "All Tests Passed."
"""


































































































































