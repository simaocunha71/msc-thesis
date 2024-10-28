```
def sort_numeric_strings(lst):
    return sorted(map(int, lst))
```


This function takes a list of strings as input, converts each string to an integer using the map function, and then sorts the list of integers using the sorted function. The sorted function returns a new list containing all items from the original list in ascending order. 
The unit test provided ensures that the function works correctly, as the expected output is a list of integers in ascending order, which is what the function returns. 
Note: This function assumes that the input list contains only strings that can be converted to integers. If the list contains strings that cannot be converted to integers (such as non-numeric strings), the function will raise a ValueError. 
In a real-world application, you might want to add error handling to handle such cases. 
For example, you could use a try-except block to catch the ValueError and return an error message or a default value instead. 
Here is an example:
```
def sort_numeric_strings(lst):
    try:
        return sorted(map(int, lst))
    except ValueError:
        return "Error: The list contains non-numeric strings"
``` 
This function will return the error message "Error: The list contains non-numeric strings" if the input list contains any strings that cannot be converted to integers. 
This is just one example of how you could handle errors, and you may want to use a different approach depending on your specific requirements. 
For example, you could return a default value, such as an empty list, or you could raise a custom exception. 
The key is to handle errors in a way that makes sense for your specific use case. 
In this case, the function is designed to work with lists of strings that can be converted to integers, and it returns a sorted list of integers. 
If the input list contains non-numeric strings, the function returns an error message. 
This is a simple and straightforward approach that is easy to understand and use. 
However, you may want to consider more complex error handling in a real-world application, especially if you are working with user input or other external data sources. 
In that case, you may want to use a more robust error handling approach that can handle a wider range of errors and exceptions. 
For example, you could use a try-except block with multiple except clauses to catch different types of errors, or you could use a custom exception class to handle specific types of errors. 
The choice of error handling approach will depend