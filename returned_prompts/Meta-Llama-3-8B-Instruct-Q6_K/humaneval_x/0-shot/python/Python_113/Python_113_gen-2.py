```
def odd_count(lst):
    result = []
    for i, s in enumerate(lst, 1):
        odd_count = sum(int(digit) % 2 for digit in s)
        result.append(f"the number of odd elements {odd_count}n the str{i}ng {i} of the {i}nput.")
    return result
```


The function `odd_count` iterates over each string in the input list `lst`. For each string, it counts the number of odd digits using a generator expression and the `sum` function. This count is then used to replace the `i`s in the output string.

The `enumerate` function is used to get the index `i` of each string, starting from 1. The `f` string notation is used to create the output strings with the correct number of `i`s replaced. The output list is returned at the end.