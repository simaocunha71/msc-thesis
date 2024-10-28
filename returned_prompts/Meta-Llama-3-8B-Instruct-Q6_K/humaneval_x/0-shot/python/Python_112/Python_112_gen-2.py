```
def reverse_delete(s,c):
    s = [i for i in s if i not in c]
    s = ''.join(s)
    return (s, s == s[::-1])
```


```
print(reverse_delete("abcde", "ae"))  # ('bcd', False)
print(reverse_delete("abcdef", "b"))  # ('acdef', False)
print(reverse_delete("abcdedcba", "ab"))  # ('cdedc', True)
```


The function `reverse_delete` takes two strings `s` and `c` as input. It first creates a new string `s` that contains all characters from `s` except those that are in `c`. This is done using a list comprehension that checks if each character in `s` is not in `c`. The list is then converted back to a string using the `join` method.

Then it checks if the result string is palindrome or not. This is done by comparing the result string with its reverse. If they are the same, the string is palindrome, otherwise not. The result is returned as a tuple, where the first element is the result string and the second element is a boolean indicating whether the string is palindrome or not.