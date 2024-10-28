```
def will_it_fly(q, w):
    if q == q[::-1]:  # check if the list is balanced (palindromic)
        return sum(q) <= w  # if it's balanced, check if the sum is less than or equal to w
    else:
        return False  # if it's not balanced, return False
```