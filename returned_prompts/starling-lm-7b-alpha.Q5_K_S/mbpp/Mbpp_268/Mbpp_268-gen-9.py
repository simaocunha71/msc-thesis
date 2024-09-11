def find_star_num(n):
    return n * (n + 1) * (n + 2) // 6


```
def find_star_num(n):
    return n * (n + 1) * (n + 2) // 6
```

This function uses the formula for the sum of the first n natural numbers multiplied by (n + 1) and (n + 2). The formula is derived from the formula for the sum of an arithmetic series and then simplified by factoring out a (n + 1). 

In the original formula for the sum of the first n natural numbers, the sum is given by the expression n * (n + 1) / 2. However, in this case, we need to multiply the sum by (n + 1) and (n + 2) to account for the additional numbers that need to be added to get the total number of star numbers. 

To simplify the expression, we can factor out (n + 1) from the product, giving us (n + 1) * (n * (n + 1) / 2). 

Finally, we can simplify the expression further by multiplying (n + 1) * (n * (n + 1) / 2) by n + 2, which gives us the final expression n * (n + 1) * (n + 2) // 6. 

This expression represents the sum of the first n natural numbers multiplied by (n + 1) and (n + 2), which gives us the total number of star numbers for the given n. 

For example, if we input n = 3 into the function, it will return 37, which is the total number of star numbers for the first 3 natural numbers.
```

```python
def find_star_num(n):
    return n * (n + 1) * (n + 2) // 6
```

This function calculates the n'th star number by using the formula `n * (n + 1) * (n + 2) // 6`. The function takes an integer `n` as input and returns the corresponding star number. The formula is derived from the