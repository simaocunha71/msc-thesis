```
def string_to_list(s):
    return s.split()
```
This function uses the built-in `split()` method of strings in Python, which splits a string into a list where each word is a list item. The default separator is the space character. 

For example, if the input string is "python programming", the function will return `['python','programming']`. 

The unit test `assert string_to_list("python programming")==['python','programming']` confirms this.  It checks if the output of the function is equal to the expected output `['python','programming']`. If the output is not equal, the test will fail, indicating that the function is not working correctly.  In this case, the function is working correctly. 

The function is simple and efficient, making it a good solution for this problem.  It does not require any additional libraries or modules, as the `split()` method is a built-in Python method.  It also does not have any unnecessary complexity, making it easy to understand and maintain.  Therefore, it is a good solution for the problem. 