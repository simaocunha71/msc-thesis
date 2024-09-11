"""
def count_Set_Bits(n):
    count = 0
    while(n):
        count += n & 1
        n = n >> 1
    return count
"""

def count_Set_Bits(n):
    count = 0
    while(n):
        count += n & 1
        n = n >> 1
    return count

def test_count_Set_Bits():
    assert count_Set_Bits(2) == 1
    print("All Test Passed")

test_count_Set_Bits()


# Made By Mostafa_Khaled
"""







"""


```

```