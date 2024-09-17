```
def count_Substrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if sum(int(digit) for digit in substring) == len(substring):
                count += 1
    return count
```


This function iterates over all substrings of the given string `s` and checks if the sum of the digits in the substring is equal to its length. If it is, it increments the count. The function returns the total count of such substrings. 

The unit test `assert count_Substrings('112112') == 6` indicates that the function should return 6 for the input '112112'. This is because the substrings '1', '1', '11', '11', '12', '11', '1', '1', '1', '1' have the sum of digits equal to their length. The function correctly counts these substrings. 





This function has a time complexity of O(n^2*m) where n is the length of the string and m is the maximum length of a substring. This is because it iterates over all substrings of the string and for each substring, it calculates the sum of its digits. The space complexity is O(1) as it only uses a constant amount of space. 





The function could be optimized by using a sliding window approach, which would reduce the time complexity to O(n*m). This would be achieved by iterating over the string and for each character, it would calculate the sum of the digits in the current window and update the count accordingly. This approach would be more efficient for large inputs. 





However, the current function is simple and easy to understand, and it works correctly for all inputs. Therefore, it is a good solution for this problem. 





The function could also be optimized by using a dictionary to store the sum of digits for each substring. This would reduce the time complexity to O(n*m) and the space complexity to O(m). This approach would be more efficient for large inputs. 





Here is the optimized function:

```
def count_Substrings(s):
    count = 0
    sum_dict = {}
    for i in range(len(s)):
        sum_val = 0
        for j in range(i, len(s)):
            sum_val += int(s[j])
            if sum_val == j - i + 1