
def max_sum_increasing_subseq(nums: list, i: int, k: int, n: int) -> int:
    # Initialize result
    result = 0

    # Create an auxiliary array and fill it with 1s
    aux = [1] * n

    # Build the auxiliary array for all elements
    # after index i
    for j in range(i+1, n):
        for t in range(j):
            if (nums[j] > nums[t]) and (aux[j] < aux[t] + 1):
                aux[j] = aux[t] + 1

    # Add the kth element to the maximum sum
    result = nums[k] + aux[k]

    return result


