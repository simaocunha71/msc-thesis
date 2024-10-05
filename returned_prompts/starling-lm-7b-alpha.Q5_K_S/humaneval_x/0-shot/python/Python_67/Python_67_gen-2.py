
def fruit_distribution(s,n):
    s=s.split()
    return n - int(s[0][0]) - int(s[1][0])







```
fruit_distribution("5 apples and 6 oranges", 19)
```

This code defines a function `fruit_distribution` that takes a string `s` and an integer `n` as input. The string `s` represents the number of apples and oranges in the basket, while the integer `n` represents the total number of fruits in the basket. 

The function first splits the string `s` into a list of substrings using the `split()` method. This allows us to extract the number of apples and oranges from the string. 

Then, the function returns the result of subtracting the total number of apples and oranges from `n`. This gives us the total number of mango fruits in the basket. 

To test the function, the code calls `fruit_distribution` with the input `"5 apples and 6 oranges"` and `19`. This should return the result `8`, as there are 5 apples, 6 oranges, and 8 mango fruits in the basket. 

You can use this code as a starting point for solving the problem, and modify it as needed to handle different inputs and requirements.
```

```