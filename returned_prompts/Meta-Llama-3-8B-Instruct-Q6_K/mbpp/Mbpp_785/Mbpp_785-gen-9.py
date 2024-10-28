```
def tuple_str_int(t):
    return tuple(map(int, t.strip('()').split(',')))
```


This solution works by first removing the parentheses from the string using the `strip` method. Then it splits the string into a list of strings using the `split` method with a comma as the separator. The `map` function is then used to convert each string in the list to an integer, and the `tuple` function is used to convert the list of integers back into a tuple. The result is the original tuple but with strings converted to integers. 

The unit test `assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)` ensures that the function works correctly. It checks that the input string is converted to the expected tuple of integers. 

This solution assumes that the input string is a valid tuple string, i.e., it contains only digits, commas, and parentheses, and that the parentheses are properly balanced. If the input string is invalid, the function may raise an error or produce unexpected results. 

In a real-world application, you would want to add error handling to deal with invalid input strings. For example, you could use a try-except block to catch any exceptions that are raised when converting the strings to integers. You could also add input validation to check that the input string is a valid tuple string before attempting to convert it. 

Here is an example of how you could modify the function to add error handling and input validation:
```
def tuple_str_int(t):
    try:
        t = t.strip('()').split(',')
        return tuple(map(int, t))
    except ValueError:
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
```


This modified function will return `None` if the input string is invalid or if there is an error when converting the strings to integers. It will also print an error message if an unexpected error occurs. You could modify the function further to return a more informative error message or to handle specific types of errors differently. 

In general, it's a good idea to add error handling and input validation to your functions to make them more robust and reliable. This can help prevent unexpected errors and make your code easier to use and maintain. 