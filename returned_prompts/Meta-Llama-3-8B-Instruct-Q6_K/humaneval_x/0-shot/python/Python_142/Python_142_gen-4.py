The solution is written in Python. It uses list comprehension to square the entries if the index is a multiple of 3, cube the entries if the index is a multiple of 4 and not a multiple of 3. Then it sums up all the entries.

```
def sum_squares(lst):
    return sum((x**2 if i%3==0 else x**3 if i%4==0 and i%3!=0 else x for i,x in enumerate(lst)))
```



Explanation:
- `enumerate(lst)` returns a tuple containing a count (from the start which defaults to 0) and the values obtained from iterating over the sequence (`lst`).
- `i%3==0` checks if the index is a multiple of 3.
- `i%4==0 and i%3!=0` checks if the index is a multiple of 4 but not a multiple of 3.
- `x**2` squares the number.
- `x**3` cubes the number.
- `x` leaves the number as it is.
- `sum` adds up all the numbers. 





Test cases:
```
print(sum_squares([1,2,3])) # Output: 6
print(sum_squares([])) # Output: 0
print(sum_squares([-1,-5,2,-1,-5])) # Output: -126
``` 





This function will work correctly for all test cases. It handles the edge case of an empty list and returns 0 as expected. It also correctly handles the case where the input list is not empty. The function also correctly handles the case where the input list contains negative numbers. 