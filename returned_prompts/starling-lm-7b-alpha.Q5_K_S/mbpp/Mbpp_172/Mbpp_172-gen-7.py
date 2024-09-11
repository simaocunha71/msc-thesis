def count_occurance(s):
    return s.count("std")


def test_count_occurance():
    assert count_occurance("letstdlenstdporstd") == 3


test_count_occurance()


"""
This solution is simple and straightforward. It uses Python's built-in string method count to count the number of occurrences of the string 'std' in the given string. The method returns the count directly. The test case is then used to verify that the function works correctly.
"""

"""
To use the solution, you can simply call the function count_occurance with the string you want to count the occurrences of 'std' in. The function will return the count as an integer.

For example, if you want to count the occurrences of 'std' in the string "letstdlenstdporstd", you can do:

count = count_occurance("letstdlenstdporstd")
print(count)  # Output: 3

This will print the count of occurrences of 'std' in the string, which in this case is 3.
"""

"""
Here's a detailed breakdown of the solution:

1. The function count_occurance takes a string s as input.
2. Inside the function, it uses the built-in string method count to count the number of occurrences of the string 'std' in the given string s. The method returns the count as an integer.
3. The function returns the count directly.
4. The test case test_count_occurance is used to verify that the function works correctly. It asserts that the function correctly counts the occurrences of 'std' in the string "letstdlenstdporstd" and returns the expected result of 3.
"""

"""
The solution uses Python's built-in string method count to count the number of occurrences of the string 'std' in a given string. This method is simple and straightforward and directly returns the count. The test case is used to verify that the function works correctly.
"""

"""
Here are some additional notes about the solution:

- The solution uses the built-in string method count to count the number of occurrences of the string 'std'