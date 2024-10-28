```
def return_sum(dict):
    total = 0
    for value in dict.values():
        total += value
    return total
```



Explanation:
The problem is asking to write a function that takes a dictionary as input and returns the sum of all its values. 

The unit test `assert return_sum({'a': 100, 'b':200, 'c':300}) == 600` helps to clarify that we need to sum all the values in the dictionary. 

In Python, we can solve this problem by iterating over the values of the dictionary using the `.values()` method and summing them up. This is what the `return_sum` function does. It initializes a variable `total` to 0, then iterates over each value in the dictionary, adding it to `total`. Finally, it returns the total sum. 

The unit test ensures that the function works correctly by checking that the sum of the values in the dictionary `{'a': 100, 'b':200, 'c':300}` is indeed 600. 

This solution is concise and efficient, as it uses built-in dictionary methods and a simple loop. It is also easy to understand and modify, making it a good solution for this problem. 

Note that this solution assumes that the dictionary values are numbers. If the dictionary values are not numbers, the function may raise an error or produce unexpected results. In a real-world application, you would need to add error handling to handle non-numeric values. 

Also, this solution does not handle the case where the dictionary is empty. In a real-world application, you would need to add a check for this case and return a suitable value, such as 0. 

Finally, this solution is case-sensitive, so it treats 'a' and 'A' as different keys. If you want to ignore case, you would need to convert the keys to a standard case before using them. 

In summary, this solution is a good starting point, but you would need to add error handling and case-insensitive handling to make it robust and suitable for real-world use. 