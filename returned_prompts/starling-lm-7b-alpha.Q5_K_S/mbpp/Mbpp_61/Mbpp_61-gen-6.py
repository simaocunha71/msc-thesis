```
def count_Substrings(s):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    n = len(s)
    res = 0
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += int(s[j])
            if sum == j-i+1:
                res += 1
    return res
```

Explanation:
The function count_Substrings(s) takes a string s as input and returns the number of substrings with the sum of digits equal to their length. 

The function first checks if the length of the string s is zero, in which case it returns zero, as there are no substrings. If the length of the string s is one, it returns one, as there is only one substring in this case, which is the string itself. 

For strings with length greater than one, the function initializes a variable res to keep track of the number of substrings with the desired property. It then iterates over all possible substrings of the string s using two nested loops. 

For each substring, the function computes the sum of the digits in the substring by iterating over its indices and adding the corresponding digit to the sum. If the sum is equal to the length of the substring minus the starting index of the substring plus one, the function increments the variable res by one. 

Finally, the function returns the value of res, which represents the number of substrings with the sum of digits equal to their length in the input string s.

The given assert statement tests the function by passing the string '112112' to it and verifies that the returned value is equal to 6, as expected.

Overall, the function count_Substrings(s) provides a way to count the number of substrings with the sum of digits equal to their length in a given string s.

```

```

```python

```

```

```python

```

```

```

```

```
```

```python
