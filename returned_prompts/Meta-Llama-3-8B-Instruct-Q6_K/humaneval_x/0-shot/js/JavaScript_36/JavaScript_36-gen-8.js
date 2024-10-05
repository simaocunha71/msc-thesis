Here is a Python solution for the problem:

```python
def fizzBuzz(n):
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            str_i = str(i)
            count += str_i.count('7')
    return count
```

This function iterates over all integers less than `n` and checks if they are divisible by 11 or 13. If they are, it converts the integer to a string and counts the number of '7's in the string. It then adds this count to the overall count and returns it at the end. 

Here are the results for the examples you provided:

```python
print(fizzBuzz(50))  # Output: 0
print(fizzBuzz(78))  # Output: 2
print(fizzBuzz(79))  # Output: 3
```


The time complexity of this solution is O(n), where n is the input number. This is because we are iterating over all integers less than n. The space complexity is O(1), as we are using a constant amount of space to store the count and the current integer. 