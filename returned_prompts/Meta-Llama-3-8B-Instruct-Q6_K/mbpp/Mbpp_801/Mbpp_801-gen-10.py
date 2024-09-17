```
def three_equal(a, b, c):
    count = 0
    if a == b:
        if a == c:
            count = 3
        else:
            count = 2
    else:
        if a == c:
            count = 2
        elif b == c:
            count = 2
    return count
```


This function takes three integers as input and returns the number of equal numbers among them. It first checks if the first two numbers are equal, then checks if the third number is equal to either of the first two. It increments the count accordingly. The unit test `assert test_three_equal(1,1,1) == 3` ensures that the function correctly returns 3 when all three numbers are equal. 

This function can be further simplified by returning the sum of the counts of each pair of equal numbers:
```
def three_equal(a, b, c):
    return sum(1 for x in [a, b, c] for y in [a, b, c] if x == y)
```


This version of the function uses a generator expression to iterate over all pairs of numbers and count the number of pairs that are equal. It is more concise and can be more efficient for large inputs. However, it is less readable and may be less understandable for someone who is not familiar with generator expressions. 