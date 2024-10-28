Here is the Python code to solve the problem:

```Python
def ReverseDelete(s, c):
    new_s = ""
    for char in s:
        if char not in c:
            new_s += char
    return (new_s, new_s == new_s[::-1])
```

This function loops through each character in the string `s`. If the character is not in `c`, it adds it to a new string `new_s`. At the end, it returns a tuple containing `new_s` and a boolean indicating whether `new_s` is a palindrome. 

Here's how you can use it:

```Python
print(ReverseDelete("abcde", "ae"))  # Output: ('bcd', False)
print(ReverseDelete("abcdef", "b"))  # Output: ('acdef', False)
print(ReverseDelete("abcdedcba", "ab"))  # Output: ('cdedc', True)
```

In Python, the `in` operator checks if a character is in a string. The `[::-1]` is used to reverse the string. The `==` operator checks if two strings are equal. 

This function has a time complexity of O(n), where n is the length of the string `s`. This is because it needs to iterate through each character in `s`. The space complexity is also O(n), as it needs to store the new string `new_s`. 