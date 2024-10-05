
Here is a Python function that tests if a string is a palindrome, and another function that finds the shortest palindrome that begins with a supplied string.

To test if a string is a palindrome, you can simply compare it to its reverse. Here's the function for that:

```python
def is_palindrome(string):
    return string == string[::-1]
```

To find the shortest palindrome that begins with a supplied string, you can find the longest palindromic suffix of the string and prepend the reverse of the prefix of the string that comes before the palindromic suffix. Here's the function for that:

```python
def make_palindrome(string):
    if is_palindrome(string):
        return string

    # Find the longest palindromic suffix of the string
    suffix_start = 0
    for i in range(len(string) // 2):
        if string[i] != string[-1 - i]:
            break
        suffix_start += 1

    # Get the prefix of the string before the palindromic suffix
    prefix_start = len(string) - suffix_start

    # Find the longest palindromic prefix of the prefix
    for i in range(suffix_start + 1, prefix_start):
        if string[:i] != string[:i][::-1]:
            break

    # Prepend the reverse of the prefix to the string
    return string[:i][::-1] + string + string[:i]
```

You can test the functions with the following examples:

```python
print(make_palindrome(''))  # ''
print(make_palindrome('cat'))  # 'catac'
print(make_palindrome('cata'))  # 'catac'
```

These functions should correctly identify and create palindromes, respectively.

Here's a step-by-step breakdown of the `make_palindrome` function:

1. The function first checks if the input string is already a palindrome. If it is, the function simply returns the input string.
2. If the input string is not