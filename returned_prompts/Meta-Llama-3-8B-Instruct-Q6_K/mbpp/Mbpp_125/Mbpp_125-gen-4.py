```
def find_length(s):
    max_diff = 0
    diff = 0
    zeros = 0
    ones = 0
    for i in range(len(s)):
        if s[i] == '0':
            zeros += 1
        else:
            ones += 1
        diff = abs(zeros - ones)
        max_diff = max(max_diff, diff)
    return max_diff
```


The problem asks to find the maximum difference between the number of 0s and number of 1s in any sub-string of a given binary string.

The function `find_length` initializes `max_diff` as 0, `diff` as 0, `zeros` as 0, and `ones` as 0. It then iterates over the binary string. For each character, it updates `zeros` and `ones` accordingly. It calculates the difference `diff` between `zeros` and `ones` and updates `max_diff` if `diff` is greater than `max_diff`. Finally, it returns `max_diff`.

The unit test `assert find_length("11000010001") == 6` helps to understand the problem better. It suggests that the function should return the maximum difference between the number of 0s and number of 1s in any sub-string of the given binary string. In this case, the maximum difference is 6. 

The function works by maintaining a running total of the number of 0s and 1s in the current window and updating the maximum difference as it goes. This approach ensures that the function has a time complexity of O(n), where n is the length of the input string. 





# 3. Maximum sum of subarray of size k

