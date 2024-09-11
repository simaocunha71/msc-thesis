"""
def Find_Min_Length(l):
    min_length = len(l[0])
    for i in range(len(l)):
        if len(l[i]) < min_length:
            min_length = len(l[i])
    return min_length
"""

def Find_Min_Length(l):
    return min(map(len, l))

assert Find_Min_Length([[1],[1,2]]) == 1


"""
def Find_Min_Length(l):
    if len(l) == 0:
        return 0
    else:
        if len(l) == 1:
            return len(l[0])
        else:
            if len(l[0]) < len(l[1]):
                return Find_Min_Length(l[0:1])
            else:
                return Find_Min_Length(l[1:])
"""

```

I think the above code should be able to solve the problem. The idea is to use Python's built-in min function to find the minimum length among a list of integers. However, in this case, we are given a list of lists, so we need to use map to apply the len function to each sublist, and then use min to find the minimum length among these sublists.

Here's a step-by-step breakdown of the code:

1. Define the function Find_Min_Length that takes a list l as input.
2. Use the built-in min function to find the minimum length among all the sublists in l. This is done by applying the len function to each sublist using map, and then passing the result to min.
3. Return the minimum length found.
4. Add a test case to check if the function works correctly. This is done using the assert keyword, which checks if the output of the function is equal to the expected output.

In this case, the expected output is 1, because the smallest sublist in the given list of lists is [1].

I hope this helps! Let me know if you have any more questions.
```

```python
def Find_Min_Length(l):
    if len(l) == 0