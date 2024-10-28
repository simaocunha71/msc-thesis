def remove_all_spaces(s):
    return s.replace(" ","")  # or return s.replace(' ', '') if python version is less than 3.6

# Testing the function
assert remove_all_spaces('python  program')==('pythonprogram')  # Test case
print(remove_all_spaces('python  program'))  # Output: pythonprogram

Explanation: 
The function `remove_all_spaces` takes a string `s` as input and returns the same string but with all spaces removed. This is achieved by using the `replace` method of the string class in Python, which replaces all occurrences of a specified string (in this case, a space) with another string (in this case, an empty string). This effectively removes all spaces from the input string.

The unit test `assert remove_all_spaces('python  program')==('pythonprogram')` ensures that the function works correctly by comparing the output of the function with the expected output. 

The print statement at the end is used to test the function with a sample input and verify that it produces the expected output. 





Note: 
The `replace` method in Python is case sensitive. If you want to remove all spaces regardless of whether they are uppercase or lowercase, you should use `replace(' ', '')` instead. If you are using a Python version less than 3.6, you should use `replace(' ', '')` as the `replace` method was changed in Python 3.6.