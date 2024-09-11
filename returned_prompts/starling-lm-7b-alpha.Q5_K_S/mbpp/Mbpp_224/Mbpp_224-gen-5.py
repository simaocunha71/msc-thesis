"""
def count_Set_Bits(n):
    cnt = 0
    while n:
        cnt += n & 1
        n >>= 1
    return cnt

def test_count_Set_Bits():
    assert count_Set_Bits(2) == 1

test_count_Set_Bits()
"""

