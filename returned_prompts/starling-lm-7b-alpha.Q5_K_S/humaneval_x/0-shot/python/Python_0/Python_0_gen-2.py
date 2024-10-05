    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < threshold:
                return True
    return False


# These "asserts" using only for self-checking and not necessary for auto-grading
if __name__ == "__main__":
    import sys
    from typing import List
    assert has_close_elements([1.0, 2.0, 3.0], 0.5) == False
    assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) == True
    assert has_close_elements([1.0, 2.0, 3.0], 0.7) == False
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0], 0.3) == False
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0], 0.4) == True
    # Checking for edge cases
    assert has_close_elements([-1000.0, 0.0, 1.0], 0.0000000000000001) == True
    assert has_close_elements([-1000.0, 0.0, 1.0], 0.00000000000000001) == False
    print(sys.getrecursionlimit())
    sys.setrecursionlimit(10 ** 6)
    print(sys.getrecursionlimit())


# Testing recursion limit
def test_recursion():
    def factorial(n: int) -> int:
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    assert factorial(5) == 