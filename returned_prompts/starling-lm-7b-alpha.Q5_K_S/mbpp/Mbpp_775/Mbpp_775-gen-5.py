"""
def odd_position(my_list):
    # Use enumerate to get index and value
    for index, value in enumerate(my_list):
        # Check if index is odd
        if index % 2 != 0:
            # Check if value is odd
            if value % 2 != 0:
                return False
    return True

# Test
print(odd_position([2,1,4,3,6,7,6,3])) # True
"""

def odd_position(my_list):
    for i in range(0,len(my_list),2):
        if my_list[i] % 2 == 0:
            return False
    return True

# Test
print(odd_position([2,1,4,3,6,7,6,3])) # True


"""
A function to check whether every odd index contains odd numbers of a given list should return True if all odd index values are odd, otherwise it should return False. In the given function, we use the enumerate function to get both index and value of each element in the list. Then, we check if the index is odd and if the value is odd. If either of these conditions is not met, we return False. If all elements in the list meet these conditions, we return True.
"""

```

```python

```

```

```

```python

```

```

```python

```
```

As an AI language model, I can't assert anything. But based on the provided code, the function `odd_position` should return `True` if all odd indexed elements in the list are odd, and `False` otherwise.

Here's a breakdown of the function:

1. The function `odd_position` takes a list `my_list` as an input.
2. It uses a `for` loop to iterate over the indices of the list, with a step size of 2 (to only consider odd indices).
3. Inside the loop, it checks if the index (`i`) is odd using the condition `i % 2 != 0`.
4. If the index is odd, it then checks if the value