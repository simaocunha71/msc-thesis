```
def how_many_times(string: str, substring: str) -> int:
    count = start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos != -1:
            start = pos + 1
            count += 1
        else:
            break
    return count
```


Explanation:

1. Initialize `count` to 0, which will store the number of times the substring is found in the string.
2. Initialize `start` to 0, which will be used to keep track of the starting position of the substring in the string.
3. Use a while loop to iterate over the string, starting from the beginning (`start = 0`).
4. Inside the loop, use the `find` method to search for the substring starting from the current `start` position. If the substring is found, update `start` to the position after the found substring (`start = pos + 1`) and increment `count` by 1.
5. If the substring is not found, break out of the loop.
6. Return the final value of `count`, which represents the number of times the substring can be found in the original string.

Note: The `find` method returns the index of the first occurrence of the substring if it is found, and -1 if it is not found. This allows us to easily check if the substring was found and update the `start` position accordingly.