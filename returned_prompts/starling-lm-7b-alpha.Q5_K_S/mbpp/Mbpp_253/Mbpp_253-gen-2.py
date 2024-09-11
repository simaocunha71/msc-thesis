"""
def count_integer(lst):
    count = 0
    for i in lst:
        if isinstance(i, int):
            count += 1
    return count
"""

def count_integer(lst):
    count = 0
    for i in lst:
        if isinstance(i, int):
            count += 1
    return count

# assert count_integer([1,2,'abc',1.2]) == 2
print(count_integer([1,2,'abc',1.2]))
# print(count_integer([1,2,3,4,5]))

def test_count_integer():
    assert count_integer([1,2,'abc',1.2]) == 2
    assert count_integer([1,2,3,4,5]) == 5
    print("All Tests Passed")

test_count_integer()

```
    

























```

```