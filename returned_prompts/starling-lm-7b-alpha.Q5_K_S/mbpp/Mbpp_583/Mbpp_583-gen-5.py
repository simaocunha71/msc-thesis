```
# O(n^2)
def catalan_number(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        c = [0] * (n + 1)
        c[0] = 1
        c[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                c[i] += c[j] * c[i-1-j]
        return c[n]
```

# O(n)
```
def catalan_number(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n % 2 == 0:
        return catalan_number(n - 1) * catalan_number(n / 2)
    else:
        return catalan_number(n - 2) * catalan_number((n + 1) / 2)
```



Explanation:

The Catalan numbers are a sequence of natural numbers that have many applications in combinatorics, especially in the study of various types of trees.

The first few Catalan numbers are 1, 1, 2, 5, 14, 42, 132, ...

Here are some properties of Catalan numbers:

1. The nth Catalan number is the number of non-crossing, self-avoiding lattice paths from (0,0) to (2n,0) that stay above the x-axis.
2. The nth Catalan number is the number of ways to arrange the parentheses in a valid way in an expression consisting of 2n + 1 parts, each of which is either a left parenthesis ( or a right parenthesis ).
3. The nth Catalan number is the number of ways to represent an integer less than or equal to n as the sum of distinct positive integers.
4. The nth Catalan number is the number of ways to arrange n objects in a circle so that they are all distinct.
5. The nth Catalan number is the number of non-associ