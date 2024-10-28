def minimum(a, b):
    if a <= b:
        return a
    else:
        return b
assert minimum(1,2) == 1
print(minimum(1,2))  # Output: 1

Explanation:
This function takes two numbers as input and returns the minimum of the two. It uses a simple if-else statement to compare the two numbers and return the smaller one. The unit test `assert minimum(1,2) == 1` ensures that the function is working correctly. The `print(minimum(1,2))` statement is used to print the output of the function, which is 1 in this case.  The function is tested by checking if the minimum of 1 and 2 is 1, which is expected output.  If the function returns anything other than 1, the test will fail and an error message will be printed.  If the function returns 1, the test will pass and no error message will be printed.  This ensures that the function is working correctly.  The function can be used with any two numbers and it will always return the minimum of the two.  



