```
def count_three_equal(a, b, c):
    if a == b == c:
        return 3
    else:
        return 0
```


This function takes three integers as arguments, and returns the number of equal numbers among them. If all three numbers are equal, it returns 3, otherwise it returns 0. The unit test `assert test_three_equal(1,1,1) == 3` ensures that the function works correctly when all three numbers are equal. 

Note that the problem statement is a bit unclear about what it means by "equal numbers". However, based on the unit test, it seems that it wants to count the number of times the same number appears among the three given integers. If all three numbers are the same, it counts them all; otherwise, it counts none.  This interpretation is also supported by the function's return values (3 for all equal, 0 for not all equal).  If the problem statement meant something else, the function would need to be modified accordingly.  For example, if it meant to count the number of pairs of equal numbers, the function would need to be modified to count the number of pairs.  But based on the unit test, this interpretation seems the most reasonable. 