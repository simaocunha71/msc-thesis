```
def string_to_list(s):
    return s.split()
```


Note: The unit test `assert string_to_list("python programming")==['python','programming']` suggests that the input string should be split on the space character. The `split()` function in Python is used to split a string into a list where each word is a list item. It takes an optional argument which is the separator. By default, it is a space. So, we don't need to specify it explicitly. The function `string_to_list` simply calls the `split()` function on the input string `s` and returns the result. 
Example: If you call `string_to_list("python programming")`, it will return `['python', 'programming']`. 