"""
To find perfect squares, you can use the fact that the square root of a perfect square is an integer. In other words, if you take the square root of a number and the result is an integer, then that number is a perfect square.

Here's a function that implements this logic:

def perfect_squares(start, end):
    squares = []
    for i in range(start, end + 1):
        if int(i ** 0.5) ** 2 == i:
            squares.append(i)
    return squares

You can call the function like this: perfect_squares(1, 30). The function will return a list of all the perfect squares between 1 and 30 (inclusive): [1, 4, 9, 16, 25].
"""

# Python3 program to print all perfect squares in a given range

def perfectSquares(start, end):
    squares = []
    for i in range(start, end + 1):
        if int(i ** 0.5) ** 2 == i:
            squares.append(i)
    return squares

# Driver program
if __name__=='__main__':
    print(perfectSquares(1,30))



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

