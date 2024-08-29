def max_sub_array_sum(arr, n):
    max_so_far = arr[0]
    curr_max = arr[0]

    for i in range(1, n):
        curr_max = max(arr[i], curr_max + arr[i])
        max_so_far = max(max_so_far, curr_max)

    return max_so_far

print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8))
<jupyter_output>
7
<jupyter_text>
Explanation:The function `max_sub_array_sum` uses the Kadane's algorithm to find the sum of the largest contiguous sublist in the given list. The algorithm works by keeping track of the maximum sum and the current maximum sum at each step. At each step, the current maximum sum is updated to be the maximum of the current element and the sum of the current element and the current maximum sum. The maximum sum is then updated to be the maximum of the current maximum sum and the maximum sum found so far.The function returns the maximum sum found.  Unit Test
<jupyter_code>
def test_max_sub_array_sum():
    assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
    assert max_sub_array_sum([1, 2, 3, 4, -10], 5) == 7
    assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
    assert max_sub_array_sum([10, -10, 20, -40, 50], 5) == 60
    assert max_sub_array_sum([-1, -2, -3, -4, -5], 5) == -1

test_max_sub_array_sum()
<jupyter_output>
<empty_output>
