Here is the Python code for the function sum_squares:

```
def sum_squares(lst):
    sum = 0
    for i in range(len(lst)):
        if i % 3 == 0 and i % 4 != 0:
            sum += lst[i]**2
        elif i % 4 == 0 and i % 3 != 0:
            sum += lst[i]**3
        else:
            sum += lst[i]
    return sum
```
This function iterates over the list, checks the index of the current element, and applies the specified operation accordingly. The sum of all elements is then returned.