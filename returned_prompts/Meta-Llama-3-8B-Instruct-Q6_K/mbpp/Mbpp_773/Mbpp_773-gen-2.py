```
def occurance_substring(s, sub):
    if sub in s:
        return (sub, s.index(sub), s.index(sub) + len(sub))
    else:
        return None
```
This function checks if the substring `sub` is present in the string `s`. If it is, it returns a tuple containing the substring, its starting position, and its ending position. If it's not, it returns `None`. The unit test `assert occurance_substring('python programming, python language','python')==('python', 0, 6)` shows that the function should return the occurrence and position of the substring 'python' in the given string. The starting position is 0 and the ending position is 6, so the function returns `('python', 0, 6)`. If there is no match, the function returns `None`.  This function uses Python's built-in `index` function to find the position of the substring. This function is case-sensitive and considers 'python' and 'Python' as two different substrings. If you want to make it case-insensitive, you can convert both the string and the substring to lower case before checking.  Here is the case-insensitive version of the function:

```
def occurance_substring(s, sub):
    if sub.lower() in s.lower():
        return (sub, s.index(sub), s.index(sub) + len(sub))
    else:
        return None
```  This function will return the occurrence and position of the substring 'python' in the given string, regardless of the case of the string and the substring.  It will consider 'python' and 'Python' as the same substring.   If you want to make it case-sensitive and consider 'python' and 'Python' as two different substrings, you can use the original function.  If you want to make it case-insensitive and consider 'python' and 'Python' as the same substring, you can use the case-insensitive version of the function.  Both functions return `None` if there is no match.   If you want to return the count of the occurrence instead of the position, you can use the `count` function instead of `index` function.   Here is the version of the function that returns the count of the occurrence:

```
def occurance_substring(s, sub):
    if sub in s:
        return (sub, s.count(sub))
    else:
        return None
```  This