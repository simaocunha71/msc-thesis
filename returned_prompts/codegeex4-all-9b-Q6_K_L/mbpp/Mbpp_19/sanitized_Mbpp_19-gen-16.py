def test_duplicate(lst: list) -> bool:
    if len(lst) != len(set(lst)):
        return True
    else:
        return False