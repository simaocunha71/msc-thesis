```
def find_length(s):
    max_diff = 0
    count_zeros = 0
    count_ones = 0
    for i in range(len(s)):
        if s[i] == '0':
            count_zeros += 1
        else:
            count_ones += 1
        max_diff = max(max_diff, abs(count_zeros - count_ones))
    return max_diff
```





The problem is asking to find the maximum difference between the number of 0s and number of 1s in any sub-string of the given binary string. 

The unit test `assert find_length("11000010001") == 6` suggests that the maximum difference should be calculated over the entire string.

Here is the solution:

The solution initializes three variables: `max_diff` to keep track of the maximum difference, `count_zeros` to count the number of 0s, and `count_ones` to count the number of 1s. It then iterates over the string, updating `count_zeros` and `count_ones` based on the current character. The maximum difference is updated at each step by taking the maximum of the current difference and the previous maximum difference.

Finally, the function returns the maximum difference found. 

This solution has a time complexity of O(n), where n is the length of the input string. This is because it needs to iterate over the string once to find the maximum difference. The space complexity is O(1), as it only uses a constant amount of space to store the variables. 





Note: The problem statement does not explicitly mention that the sub-string can be of any length, but the unit test suggests that it can be. Therefore, the problem can be interpreted as finding the maximum difference between the number of 0s and number of 1s in any sub-string of the given binary string, including sub-strings of length 1. If the problem is intended to ask for the maximum difference in sub-strings of length greater than 1, it would need to be modified accordingly.