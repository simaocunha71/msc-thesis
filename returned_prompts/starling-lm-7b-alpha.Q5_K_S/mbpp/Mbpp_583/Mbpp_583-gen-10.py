```
def catalan_number(n):
    # Catalan number is defined as
    # C(n) = (2n)! / ((n+1)! * n!)
    return (fact(2*n))//(fact(n+1) * fact(n))

def fact(n):
    # Factorial function
    result = 1
    while (n != 1):
        result *= n
        n -= 1
    return result
```

Here is a Python program that defines a function catalan_number to return the nth Catalan number. The Catalan numbers are defined as C(n) = (2n)! / ((n+1)! * n!). The program also defines a factorial function fact to calculate factorial of a number.

The time complexity of the program is O(n) because we calculate the factorial of a number, which is O(n).

Here is an example of how to use the catalan_number function:

```python
print(catalan_number(10)) # Output: 16796
```

This will print the 10th Catalan number, which is 16796.

The Catalan numbers are interesting because they appear in a wide variety of mathematical contexts, including combinatorics, algebra, and geometry. They have many applications in computer science, including in the analysis of algorithms, the design of data structures, and the study of formal languages.

The Catalan numbers are named after the Belgian mathematician Eugène Charles Catalan. They were first studied by the Swiss mathematician Leonhard Euler in the 18th century, but Euler did not give them a name. The French mathematician Augustin Louis Cauchy is credited with discovering the formula for the Catalan numbers in the 19th century, and Catalan himself gave them the name in the 19th century as well.

```

```

In this case, the Catalan numbers are defined as C(n) = (2n)! / ((n+1)! * n!), which is a simple formula to calculate the nth Catalan number. The factorial function is used to calculate the factorial of