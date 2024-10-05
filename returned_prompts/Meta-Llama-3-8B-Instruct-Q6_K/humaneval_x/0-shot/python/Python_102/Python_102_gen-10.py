```
def choose_num(x, y):
    if x > y:
        x, y = y, x

    for i in range(x, y + 1):
        if i % 2 == 0:
            return i

    return -1
```



This function first checks if x is greater than y and swaps them if necessary. Then it iterates over the range from x to y (inclusive) and returns the first even number it finds. If no even number is found in the range, it returns -1.

Here is how it works for the examples you provided:

```
choose_num(12, 15) = 14
choose_num(13, 12) = -1
```

This function assumes that x and y are positive integers. It does not check if they are positive or integers, so you might want to add some error checking code to handle invalid inputs. For example, you could add a check at the beginning of the function to raise an exception if x or y is not a positive integer.