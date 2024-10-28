```
def simplify(x, n):
    # Convert fractions to integers
    x_int = int(eval(x.replace('/', '/')))
    n_int = int(eval(n.replace('/', '/')))

    # Check if the product is a whole number
    if x_int * n_int % 1 == 0:
        return True
    else:
        return False
```


Python code snippet for the problem. It uses the `eval` function to convert the string representation of fractions to integers. Then it checks if the product of the two integers is a whole number (i.e., has no decimal part). If it is, the function returns `True`; otherwise, it returns `False`.