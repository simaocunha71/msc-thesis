def string_to_list(string):
    return string.split()


# assert string_to_list("python programming")==['python','programming']


```

```
def string_to_list(string):
    return string.split()
```
However, you can also use the built-in Python function `split()`. Here is an example:

```python
def string_to_list(string):
    return string.split(" ")
```
This function will split the string on any whitespace character, including multiple spaces in a row.

Here is an example of how to use this function:

```python
print(string_to_list("Hello    world"))  # Prints: ['Hello', 'world']
```

This will print the list `['Hello', 'world']` from the input string `"Hello    world"`.

In addition, if you want to split the string on a specific character, you can pass that character as an argument to the `split()` function. For example, to split the string on the character `"_"`:

```python
def string_to_list(string):
    return string.split("_")
```
Here is an example of how to use this function:

```python
print(string_to_list("Hello_world"))  # Prints: ['Hello', 'world']
```

This will print the list `['Hello', 'world']` from the input string `"Hello_world"`.

In addition, you can use the `split()` function to split the string on multiple characters. For example, to split the string on both the characters `"_"` and `" "` (space):

```python
def string_to_list(string):
    return string.split("_", 1)
```
Here is an example of how to use this function:

```python
print(string_to_list("Hello_world"))  # Prints: ['Hello', 'world']
```

This will print the list `['Hello', 'world']` from the input string `"Hello_world"`.

In addition, you can use the `split()` function to split the