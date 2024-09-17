```
def count_Substrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = s[i:j]
            if sum(int(digit) for digit in substring) == len(substring):
                count += 1
    return count
```


In this function, we iterate over all possible substrings of the given string. For each substring, we check if the sum of its digits is equal to its length. If it is, we increment the count. Finally, we return the count. The unit test `assert count_Substrings('112112') == 6` ensures that the function works correctly.  It checks if there are 6 substrings with the sum of digits equal to their length in the given string '112112'.  The function should return 6 in this case, and it indeed does.  



This function has a time complexity of O(n^2), where n is the length of the string, because we are iterating over all possible substrings of the string. The space complexity is O(1), as we are not using any extra space that scales with the input size.  



This function can be optimized by using a sliding window approach instead of generating all possible substrings. However, this would make the code more complex and harder to understand. The current function is simple and easy to understand, and it works correctly for small inputs. If you need to handle large inputs, you may want to consider a more efficient algorithm.  



The unit test `assert count_Substrings('112112') == 6` ensures that the function works correctly for the given input. If the function returns the wrong result, the unit test will fail. This helps to catch errors and ensure that the function is working correctly.  



You can test the function with different inputs to ensure that it works correctly for all possible cases. For example, you can test it with strings that have different lengths, or strings that contain different characters. This will help to ensure that the function is robust and works correctly for all possible inputs.  



The function can be further improved by adding error handling to handle cases where the input is not a string. This can be done by adding a check at the beginning of the function to ensure that the input is a string, and if not, return an error message or raise an exception. This will help to ensure that the function is robust and works correctly even if the input is