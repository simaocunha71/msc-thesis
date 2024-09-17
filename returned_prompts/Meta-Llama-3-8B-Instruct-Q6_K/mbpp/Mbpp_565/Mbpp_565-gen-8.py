You can use the list comprehension in Python to split a string into characters. Here is the function:

```Python
def split(s):
    return [char for char in s]
```

This function takes a string as an argument and returns a list of characters. For example, if you call `split('python')`, it will return `['p','y','t','h','o','n']`. The unit test `assert split('python') == ['p','y','t','h','o','n']` confirms this.  This function works by iterating over each character in the input string `s` and adding it to the list. The list comprehension is a concise way to create a new list from an existing iterable (like a string). It's equivalent to a for loop that appends each item to a list.  For example, the list comprehension `[char for char in 'python']` is equivalent to:

```Python
result = []
for char in 'python':
    result.append(char)
``` 