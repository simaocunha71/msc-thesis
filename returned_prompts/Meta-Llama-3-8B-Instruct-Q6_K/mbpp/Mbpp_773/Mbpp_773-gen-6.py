```
def occurance_substring(text, substring):
    start = 0
    while start < len(text):
        pos = text.find(substring, start)
        if pos != -1:
            return substring, pos, pos + len(substring)
        start += 1
    return None
```
The function `occurance_substring` takes two parameters: `text` and `substring`. It iterates through the `text` and uses the `find` method to find the first occurrence of the `substring`. If the `substring` is found, it returns a tuple containing the `substring`, its position in the `text`, and the position plus the length of the `substring`. If the `substring` is not found, it returns `None`. 

This function is tested with the unit test `assert occurance_substring('python programming, python language','python')==('python', 0, 6)`, which ensures that the function correctly finds the occurrence and position of the `substring` in the `text`.  If the `substring` is not found, the function will return `None` as expected.  The function is case-sensitive, so it will not find the `substring` if it is in a different case.  For example, it will not find 'pYTHON' in 'python programming, python language' even though 'python' is present.  If you want a case-insensitive search, you can convert both the `text` and the `substring` to lower case or upper case before searching.  For example, `text = text.lower()` and `substring = substring.lower()`.  This will ensure that the function finds the `substring` regardless of the case.  



Here's an example of how to use the function:

```
result = occurance_substring('python programming, python language','python')
if result:
    print(f"The substring '{result[0]}' is found at position {result[1]}")
else:
    print("The substring is not found")
```

This will output:

```
The substring 'python' is found at position 0
```



This function is efficient because it uses the `find` method which has a time complexity of O(n), where n is the length of the `text`. The `find` method is implemented in C, which makes it very fast.  The function also only iterates through the `text` once, which makes it efficient even for large texts. 