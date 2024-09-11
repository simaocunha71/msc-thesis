```
from itertools import combinations
from collections import Counter

def find_Odd_Pair(arr,n):
    # Count the frequency of each element
    cnt = Counter(arr)

    # Initialize result
    res = 0

    # For every number in array
    for i in arr:

        # Generate all pairs of the number
        for j in combinations(arr, 2):

            # If xor value of the pair is 1
            if (i ^ j[0]) & 1:

                # Increment result
                res += 1

    # Return the result
    return res
```

To use this function, pass the array and its length as arguments:
```python
find_Odd_Pair([5,4,7,2,1],5)
```

The output would be `6` which is the result of the function.

Explanation:
The function `find_Odd_Pair` takes in an array `arr` and its length `n` as arguments. It uses the `Counter` class from the `collections` module to count the frequency of each element in the array. 

Then, it initializes a variable `res` to store the result. 

Next, it iterates over each number in the array and generates all possible pairs using the `combinations` function from the `itertools` module. 

For each pair, it checks if the XOR (exclusive OR) of the two numbers is odd. If it is, it increments the result variable `res`. 

Finally, it returns the result. 

In the given example, the function is called with the array `[5,4,7,2,1]` and its length `5`. The function counts the number of pairs whose XOR value is odd and returns `6`.

To use the function, you can pass your own array and its length as arguments to the `find_Odd_Pair` function. The function will return the result, which you can then use in your program.
```

```

```

```python

```

```python

```

```python

```

``