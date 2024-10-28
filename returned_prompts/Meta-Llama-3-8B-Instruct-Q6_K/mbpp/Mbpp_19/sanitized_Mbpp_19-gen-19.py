import random
def test_duplicate(arr):
    for _ in range(10):
        random.shuffle(arr)
        if len(arr) != len(set(arr)):
            return True
    return False