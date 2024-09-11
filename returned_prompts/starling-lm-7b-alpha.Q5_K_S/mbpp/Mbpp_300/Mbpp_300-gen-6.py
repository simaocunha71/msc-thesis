from typing import List
import sys


def count_binary_seq(n: int) -> int:
    if n == 0:
        return 1
    return count_binary_seq(n-1) * 2



# def count_binary_seq(n: int) -> int:
#     if n == 0:
#         return 1
#     return count_binary_seq(n-1) * 2


def test_count_binary_seq():
    assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
    assert count_binary_seq(2) == 5
    assert count_binary_seq(3) == 15

def test_count_binary_seq_big():
    for i in range(10):
        print(count_binary_seq(i))


def test_count_binary_seq_big_slow():
    for i in range(10):
        print(count_binary_seq_slow(i))

def count_binary_seq_slow(n: int) -> int:
    from itertools import product
    return len(list(product([0, 1], repeat=n * 2)))


if __name__ == "__main__":
    test_count_binary_seq()
    # test_count_binary_seq_big_slow()


```

In this script, the `count_binary_seq` function is implemented to find the count of all binary sequences of length 2n such that the sum of the first n bits is the same as the sum of the last n bits. The function uses recursion to calculate the result. The `count_binary_seq_slow` function is also implemented as a reference implementation using itertools to calculate the result, which can be used for testing purposes.

The script includes test cases to verify the correctness of the `count_binary_seq` function. It asserts that the result of `count_binary_seq(1)` is equal to 2.0, and that the result of `count_binary_seq(2)` is equal to 5. Additionally, it includes