```
def how_many_times(string: str, substring: str) -> int:
    count = start = 0
    while start < len(string):
        pos = start + 1
        while pos <= len(string):
            if string[pos - 1:pos + len(substring) - 1] == substring:
                count += 1
                start += len(substring)
                break
            pos += 1
        else:
            start += 1
    return count
```


The function `how_many_times` takes two string arguments, `string` and `substring`. It returns the number of times `substring` can be found in `string`, considering overlapping cases.

The function uses two pointers, `start` and `pos`, to traverse the `string`. It starts by setting `start` to 0, which represents the starting position for searching `substring`. The `pos` pointer is set to 1, which is the position after the starting position.

The function then enters a nested loop. The outer loop increments `start` until it reaches the end of the `string`. The inner loop increments `pos` until it finds the `substring` at the current `start` position or reaches the end of the `string`.

When the `substring` is found, the function increments the `count` by 1 and sets `start` to the position after the found `substring`. This is to consider overlapping cases.

If the `substring` is not found at the current `start` position, the function simply increments `start` to the next position and continues searching.

The function returns the total count of times `substring` can be found in `string`.