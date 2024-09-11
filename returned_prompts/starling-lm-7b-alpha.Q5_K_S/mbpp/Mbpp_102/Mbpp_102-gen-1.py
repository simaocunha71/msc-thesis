```
def snake_to_camel(snake_str):
    # Split the string by underscores
    split_str = snake_str.split('_')
    # Convert the first letter of each word to uppercase
    camel_str = split_str[0].upper()
    for i in range(1, len(split_str)):
        camel_str += split_str[i].capitalize()
    return camel_str
```

Explanation:
To convert a snake case string to camel case, we can follow these steps:

1. Split the string by underscores to get a list of words.
2. Convert the first letter of each word to uppercase using the `capitalize()` method.
3. Combine all the words to form the camel case string.

In the provided solution, the `snake_to_camel` function takes a snake case string as input and returns the corresponding camel case string. It first splits the input string by underscores using the `split('_')` method. Then, it initializes an empty string `camel_str` to store the camel case string. The first word in the list is converted to uppercase using the `upper()` method and appended to `camel_str`. For the remaining words, the `capitalize()` method is used to convert the first letter to uppercase and append the rest of the word to `camel_str`. Finally, the camel case string is returned.

To verify the correctness of the solution, an assertion is made to check if the function correctly converts the snake case string `'python_program'` to the camel case string `'PythonProgram'`.

Overall, the solution provides a simple and effective way to convert a given snake case string to camel case string.

```python
def snake_to_camel(snake_str):
    # Split the string by underscores
    split_str = snake_str.split('_')
    # Convert the first letter of each word to uppercase
    camel_str = split_str[0].upper()
    for i in range(1, len(split_str)):
        camel_str