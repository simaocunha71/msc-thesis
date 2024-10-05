

def triples_sum_to_zero(l):
    n = len(l)
    if n < 3:
        return False
    l.sort()
    for i in range(n-2):
        j = i+1
        k = n-1
        while j < k:
            if l[i] + l[j] + l[k] == 0:
                return True
            elif l[i] + l[j] + l[k] > 0:
                k -= 1
            else:
                j += 1
    return False


# Here are some tests to help you verify that your function works.
# Note that these tests might not cover all the edge cases that your function
# should handle, but they should give you a starting point.

def test_triples_sum_to_zero():
    assert triples_sum_to_zero([1, 3, 5, 0]) == False
    assert triples_sum_to_zero([1, 3, -2, 1]) == True
    assert triples_sum_to_zero([1, 2, 3, 7]) == False
    assert triples_sum_to_zero([2, 4, -5, 3, 9, 7]) == True
    assert triples_sum_to_zero([1]) == False
    assert triples_sum_to_zero([]) == False
    print("All tests passed.")

test_triples_sum_to_zero()























































































































































