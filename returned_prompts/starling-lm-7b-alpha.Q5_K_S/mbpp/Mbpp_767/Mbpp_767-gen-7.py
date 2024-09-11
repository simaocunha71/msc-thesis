"""
def get_pairs_count(lst, sum):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == sum:
                count += 1
    return count

get_pairs_count([1,1,1,1],2) == 6
"""

def get_pairs_count(lst, sum):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == sum:
                count += 1
    return count


def test():
    assert get_pairs_count([1,1,1,1],2) == 6
    print("all tests passed")


test()

```
 
```
def get_pairs_count(lst, sum):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == sum:
                count += 1
    return count


def test():
    assert get_pairs_count([1,1,1,1],2) == 6
    print("all tests passed")


test()
```
```