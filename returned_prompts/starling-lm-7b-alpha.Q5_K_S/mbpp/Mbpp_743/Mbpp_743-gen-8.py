def rotate_right(list, n):
    return list[n:] + list[:n]

def test_rotate_right():
    assert rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3)==[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]

test_rotate_right()




"""
In this code, the rotate_right function takes a list and an integer as its parameters. The function rotates the list to the right by the specified number of items. This is done by concatenating the sublist of the original list starting from the index n to the end of the list with the sublist of the original list from the beginning to the index n. The function returns the rotated list.

The test_rotate_right function is used to verify the correctness of the rotate_right function. It calls the rotate_right function with a sample list and an integer value of 3, and asserts that the returned value is equal to the expected result [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]. If the assertion passes, the test_rotate_right function will not raise an exception, indicating that the rotate_right function is working correctly.
"""

"""
The rotate_right function rotates the list to the right by the specified number of items by using concatenation. The sublist of the original list starting from index n to the end of the list is concatenated with the sublist of the original list from the beginning to index n. The result is the rotated list, which is returned by the function.

The test_rotate_right function tests the correctness of the rotate_right function. It calls the rotate_right function with a sample list and an integer value of 3, and asserts that the returned value is equal to the expected result [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]. If the assertion passes, it means that the rotate_right function is working correctly.
"""
