def is_samepatterns(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True

# assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
# assert is_samepatterns(["a","b","c"], ["d","e","f"])==False
# assert is_samepatterns(["abc"], ["abc"])==True
# assert is_samepatterns(["a","ab","abc"], ["1","2","3"])==True
# assert is_samepatterns(["a","b","c"], ["c","b","a"])==True
# assert is_samepatterns(["a","b","c"], ["c","b","d"])==False

"""
A function to determine if a number is a perfect square or not.

Explanation:
This function is implemented based on the following facts:

   1. The square root of a perfect square is an integer. For example, the square root of 4 is 2, which is an integer.
   2. If the square root of a number is not an integer, then the number is not a perfect square. For example, the square root of 3 is not an integer, so 3 is not a perfect square.

The function can be used like this:

    assert is_perfect_square(4) == True
    assert is_perfect_square(3) == False
    assert is_perfect_square(16) == True
    assert is_perfect_square(17) == False
    assert is_perfect_square(0) == False
"""

def is_perfect_square(n):
    if n < 0:
        return False
    x = n // 2
    while x * x < n:
        x += 1
    return x * x == n

# assert is_perfect_square(4) == True
# assert is_perfect_square(3) == False
# assert is_perfect_square(16) == True
