def test_duplicate(arr: list):
    return len(arr) != len(set(arr))