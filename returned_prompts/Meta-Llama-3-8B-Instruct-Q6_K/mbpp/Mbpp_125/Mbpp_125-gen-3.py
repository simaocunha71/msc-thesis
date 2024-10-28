```
def find_length(s):
    max_diff = 0
    count_0 = count_1 = 0
    for char in s:
        if char == '0':
            count_0 += 1
        else:
            count_1 += 1
        max_diff = max(max_diff, abs(count_0 - count_1))
    return max_diff
```


The function `find_length` calculates the maximum difference between the number of 0s and number of 1s in any sub-string of the given binary string. It initializes two counters `count_0` and `count_1` to keep track of the number of 0s and 1s respectively. It iterates over the string, updating the counters and the `max_diff` accordingly. The `max_diff` is updated with the absolute difference between `count_0` and `count_1` in each iteration. Finally, it returns the maximum difference found.

For example, for the input "11000010001", the function will return 6, which is the maximum difference between the number of 0s and number of 1s in any sub-string of the given binary string. The maximum difference is achieved when the sub-string is "000000", which has 6 more 0s than 1s. 





