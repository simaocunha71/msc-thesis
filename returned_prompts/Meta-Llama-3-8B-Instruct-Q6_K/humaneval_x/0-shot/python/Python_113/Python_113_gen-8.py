```
def odd_count(lst):
    result = []
    for i, s in enumerate(lst):
        odd_count = sum(1 for c in s if int(c) % 2 != 0)
        result.append(f"the number of odd elements {odd_count}n the str{i+1}ng {i+1} of the {i+1}nput.")
    return result
```


The function iterates over each string in the input list. For each string, it counts the number of odd digits by using a generator expression inside the sum function. It then constructs a string to include in the output list, using f-string formatting to replace the i's with the correct numbers. The function finally returns the list of strings.