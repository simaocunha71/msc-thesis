You can solve this problem by defining a function that takes a list of tuples as input and returns a list containing the last element of each tuple. 

Here is the Python solution for the problem:

```Python
def rear_extract(tuples):
    return [t[-1] for t in tuples]
```

This function uses a list comprehension to iterate over each tuple in the input list, and for each tuple, it extracts the last element (at index -1) and adds it to the output list. 

For example, if you call `rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)])`, the function will return `[21, 20, 19]`, which are the last elements of each tuple. 

The unit test `assert rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]) == [21, 20, 19]` confirms that the function works correctly.  It checks that the output of the function is equal to the expected output `[21, 20, 19]` when the input is `[(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]`.  If the output is not equal to the expected output, the test will fail and an error message will be displayed.  This helps to ensure that the function is working correctly.  If you run the test and it passes, you can be confident that the function is working as expected.  If you make changes to the function and the test fails, you can use the error message to help you identify and fix the problem.  This is an important part of software development, as it helps to ensure that your code is reliable and works as expected.  Without tests, it can be difficult to know whether your code is working correctly, and this can lead to bugs and errors that are difficult to track down.  By writing and running tests, you can ensure that your code is working as expected and make it easier to identify and fix problems when they occur.  This helps to improve the quality and reliability of your code, and makes it easier to maintain and update over time.  It is an important part of the software development process, and is an essential tool for any software developer.  In this case, the test is used to