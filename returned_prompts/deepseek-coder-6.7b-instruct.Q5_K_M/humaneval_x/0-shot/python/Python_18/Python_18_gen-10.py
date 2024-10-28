
```python
def how_many_times(string: str, substring: str) -> int:
    count = start = 0
    while True:
        start = string.find(substring, start) + 1
        if start > 0:
            count+=1
        else:
            return count
```

In this solution, we start from the beginning of the string and use the `find` method to find the next occurrence of the substring. If the `find` method returns a positive number, it means the substring has been found and we increase the counter. If it returns a negative number or zero, it means the substring has not been found anymore, so we return the counter.

Finally, we use a while loop to continue the search in the string.

This solution is case sensitive and does not handle the overlapping cases. For example, 'aaaa' with 'aa' will return 2 but it should return 3. To handle this situation, you can modify the solution to use a loop that starts from the found index plus 1.

Here is the modified solution:

```python
def how_many_times(string: str, substring: str) -> int:
    count = start = 0
    while True:
        start = string.find(substring, start) + 1
        if start > 0:
            count+=1
        else:
            return count
```

This solution will return the correct count for overlapping occurrences. For example, how_many_times('aaaa', 'aa') will return 3.
