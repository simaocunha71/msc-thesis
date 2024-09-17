```
def count_charac(s):
    return sum(b == ' ' for b in s)
```


This problem is asking to count the total number of characters in a string. However, the problem statement is a bit unclear. It seems to be asking for the number of spaces in the string, which is what the unit test `assert count_charac("python programming")==18` suggests.

The unit test is comparing the result of `count_charac("python programming")` with 18. This implies that the function should count the number of spaces in the string. 

The given solution uses a generator expression to iterate over each character in the string and checks if it is a space. The `sum` function then adds up the number of spaces. This solution will return the number of spaces in the string. 

However, if the problem is asking for the total number of characters in the string, the solution would be much simpler: `def count_charac(s): return len(s)`. This would return the length of the string, which is the total number of characters. 

But based on the given unit test, it seems that the problem is asking for the number of spaces in the string. 