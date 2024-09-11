"""
def even_position(nums):
    for i in range(0, len(nums), 2):
        if nums[i] % 2 != 0:
            return False
    return True

def test_even_position():
    assert even_position([3,2,1]) == False
    print("All tests passed!")

test_even_position()
"""

