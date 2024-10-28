
def make_a_pile(n):
    result = []
    while n > 0:
        result.append(n)
        if n % 2 == 0:
            n += 2
        else:
            n += 1
    return result

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    import sys
    if sys.version_info[0] < 3:
        from io import BytesIO as stream
    else:
        from io import StringIO as stream
    assert (make_a_pile(3) == [3, 5, 7]), "First example failed"
    assert (make_a_pile(4) == [4, 6, 8]), "Second example failed"
    assert (make_a_pile(2) == [2, 4]), "Third example failed"
    assert (make_a_pile(1) == [1]), "Fourth example failed"
    assert (make_a_pile(10) == [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]), "Fifth example failed"
    print("All tests passed")






































































































































































































