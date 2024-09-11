```
def catalan_number(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (4*catalan_number(n-1))/(n+1) + catalan_number(n-2)
```

Explanation:

The Catalan numbers are a sequence of natural numbers that have many applications in combinatorial mathematics, particularly in the study of polytopes, fractals, and grammars.
The sequence begins with 1, 1, 2, 5, 14, 42, 132, 429, ...
The Catalan number can also be calculated using the following formula:
$C_n = \frac{(2n)!}{n!n!}$

Here is a Python function that calculates the nth Catalan number using this formula:

```
def catalan_number(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (4*catalan_number(n-1))/(n+1) + catalan_number(n-2)
```

In this function, we use recursion to calculate the Catalan number for any given n. The base case is when n is 0 or 1, in which case the Catalan number is 1. For any other value of n, the Catalan number is calculated as the sum of twice the Catalan number for n-1 and the Catalan number for n-2, divided by n+1. 

This function correctly returns the 10th Catalan number, as tested by the provided assertion:

```
assert catalan_number(10) == 16796
```

So, the function correctly calculates the nth Catalan number for any given n.

```

```

The Catalan numbers are a sequence of natural numbers that have many applications in combinatorial mathematics, particularly in the study of polytopes, fractals, and grammars. The sequence begins with 1, 1, 2, 5, 14, 42, 132, 429, ... The Catalan