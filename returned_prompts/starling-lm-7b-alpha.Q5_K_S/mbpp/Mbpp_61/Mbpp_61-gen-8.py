```
def count_Substrings(s):
    n = len(s)
    res = 0
    for i in range(n):
        for j in range(i, n):
            if sum(map(int, s[i:j + 1])) == j - i + 1:
                res += 1
    return res
```

Explanation:
In this solution, we first initialize the result variable to 0. We then iterate through all possible substrings of the given string s. For each substring, we calculate the sum of its digits using the map and sum functions. If the sum of the digits is equal to the length of the substring, we increment the result variable by 1. Finally, we return the result variable, which gives us the total number of substrings with the sum of digits equal to their length.

The time complexity of this solution is O(n^2), where n is the length of the input string. This is because we need to iterate through all possible substrings, which requires O(n^2) time. The space complexity is O(1), as we only use a constant amount of additional memory to store the result variable.

Overall, this solution provides an efficient way to count the number of substrings with the sum of digits equal to their length in a given string.

Here is a step-by-step explanation of the code:

1. Initialize the result variable to 0. This variable will store the total number of substrings with the sum of digits equal to their length.

2. Use two nested loops to iterate through all possible substrings of the given string s. The outer loop iterates from the first character of s to the second-to-last character, and the inner loop iterates from the current character of s to the last character. This allows us to consider all possible substrings.

3. Inside the