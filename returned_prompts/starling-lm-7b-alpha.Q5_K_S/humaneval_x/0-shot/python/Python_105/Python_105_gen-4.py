    arr = by_length(arr)
    return arr


def by_length(arr):
    result = []
    arr.sort(key=lambda x: x if 1 <= x <= 9 else float('inf'))
    result = [str(x) for x in reversed(arr)]
    return [x if 1 <= x <= 9 else 'One' for x in result]


# These corpses below:
print(by_length([2, 1, 1, 4, 5, 8, 2, 3]))  # ['Eight', 'Five', 'Four', 'Three', 'Two', 'Two', 'One', 'One']
print(by_length([]))  # []
print(by_length([1, -1, 55]))  # ['One']


# These corpses below:
def by_length(arr):
    arr.sort(key=lambda x: x if 1 <= x <= 9 else float('inf'))
    return [str(x) for x in reversed(arr)]
```