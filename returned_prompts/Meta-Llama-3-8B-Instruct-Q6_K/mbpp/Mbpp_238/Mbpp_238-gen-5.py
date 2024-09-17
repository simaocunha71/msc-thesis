```
def number_of_substrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i:j+1].strip():
                count += 1
    return count
```
The function `number_of_substrings` takes a string `s` as input and returns the count of non-empty substrings. It uses two nested loops to generate all possible substrings. The `strip` method is used to remove leading and trailing whitespaces from the substring. If the substring is not empty after removing whitespaces, the count is incremented. The function returns the total count of non-empty substrings. 

The unit test `assert number_of_substrings("abc") == 6` ensures that the function correctly counts the non-empty substrings of the input string. For the input string "abc", the non-empty substrings are "a", "ab", "abc", "b", "bc", "c", and the function should return 6. 

This function has a time complexity of O(n^2) due to the use of nested loops, where n is the length of the input string. This may not be efficient for very large input strings. A more efficient solution could be implemented using dynamic programming or other techniques. 
```python
def number_of_substrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i:j+1]:
                count += 1
    return count
``` 
This function is similar to the previous one, but it uses the fact that an empty string is considered false in a boolean context. So, it checks if `s[i:j+1]` is truthy, which means it is not an empty string. This way, it avoids calling the `strip` method, which could be slower for large strings. 

The time complexity of this function is still O(n^2), but it is slightly more efficient than the previous one because it avoids the overhead of the `strip` method. 

If you want to improve the time complexity of this function, you could use a different approach, such as generating all possible substrings and then counting the non-empty ones. This would require a more complex algorithm, but it would have a time complexity of O(n). 

Here is an example of such a function:
```python
def number_of_substrings(s):
    count = 0
    for