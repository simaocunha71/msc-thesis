def square_nums(nums):
    '''
    This function takes in a list of numbers and returns a new list with the square of each number.
    '''
    return [num ** 2 for num in nums]


# Test
print(square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Test 2
def square_nums(nums):
    return [num ** 2 for num in nums]


assert square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Test 3
def square_nums(nums):
    return [num ** 2 for num in nums]


def test_square_nums():
    assert square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    assert square_nums([]) == []
    assert square_nums([-1, -2]) == [1, 4]
    assert square_nums([0]) == [0]
    assert square_nums([10, 20, 30, 40, 50]) == [100, 400, 900, 1600, 2500]


test_square_nums()

```
  1
  2
  3
  4
  5
  6
  7
  ```
  """
  def square_nums(nums