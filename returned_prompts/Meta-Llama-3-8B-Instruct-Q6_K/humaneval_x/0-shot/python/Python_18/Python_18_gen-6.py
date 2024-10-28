The task is to create a function called `how_many_times` that takes two parameters: a string and a substring. The function should return the number of times the substring can be found in the original string, counting overlapping cases.

Here is the Python solution for this problem:

```Python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    pos = 0
    while True:
        pos = string.find(substring, pos)
        if pos != -1:
            count += 1
            pos += 1
        else:
            break
    return count
```

This function works by using the `find` method of the string to find the position of the substring. If the substring is found, it increments the count and the position for the next search. This process continues until the substring is no longer found in the string. The function then returns the count.

For example, if we call `how_many_times('aaa', 'a')`, the function will return 3 because the substring 'a' can be found three times in the string 'aaa'. Similarly, if we call `how_many_times('aaaa', 'aa')`, the function will return 3 because the substring 'aa' can be found three times in the string 'aaaa'. If we call `how_many_times('', 'a')`, the function will return 0 because the substring 'a' cannot be found in an empty string. 