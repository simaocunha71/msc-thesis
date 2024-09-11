"""
def find_remainder(arr, mod):
    if len(arr) == 1:
        return arr[0] % mod
    else:
        return (find_remainder(arr[1:], mod) * arr[0]) % mod

assert find_remainder([ 100, 10, 5, 25, 35, 14 ],11) ==9
"""

def find_remainder(arr, mod):
    prod = 1
    for num in arr:
        prod = (prod * num) % mod
    return prod

assert find_remainder([ 100, 10, 5, 25, 35, 14 ],11) ==9

"""
"""
In this function, we are using a for loop to iterate over all the elements in the array. We initialize a variable "prod" to 1, and then multiply it with each element in the array and update the value of "prod". As the multiplication operation can result in a large number, we are using the modulo operator to find the remainder of the multiplication with the given modulo value. Finally, we return the value of "prod".

We are using a list comprehension to find the product of the array multiplication modulo n, which means we are multiplying each element with the previous result and taking the modulo of the result. The assert statement is used to test the function with a given example and check if the result matches the expected output.
"""

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

``