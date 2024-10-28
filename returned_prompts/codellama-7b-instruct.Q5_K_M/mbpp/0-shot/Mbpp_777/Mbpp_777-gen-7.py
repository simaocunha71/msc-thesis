def find_sum(my_list):
    return sum([i for i in my_list if my_list.count(i) == 1])

# Tests
import pytest
def test_find_sum():
    assert find_sum([1,2,3,1,1,4,5,6]) == 21
    assert find_sum([1,2,3,4]) == 10
    assert find_sum([1,2,3,4,5,6]) == 21
    assert find_sum([1,2,3,4,5,6,7]) == 28
    assert find_sum([1,2,3,4,5,6,7,8]) == 36
