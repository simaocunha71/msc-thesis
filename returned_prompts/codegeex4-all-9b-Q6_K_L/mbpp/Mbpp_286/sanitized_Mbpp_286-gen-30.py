def max_sub_array_sum_repeated(arr: list, n: int, k: int) -> int:
  # Initialize current sum and max sum
  curr_sum = 0
  max_sum = float('-inf')

  # Iterate through the array
  for i in range(len(arr)):
    # Update current sum
    curr_sum += arr[i]

    # If current sum becomes negative, reset it to 0
    if curr_sum < 0:
      curr_sum = 0

    # If current sum is greater than max sum, update max sum
    max_sum = max(max_sum, curr_sum)

  # Repeat the process k-1 times
  for _ in range(k-1):
    curr_sum -= arr[0]
    curr_sum += arr[-1]
    arr.pop(0)
    arr.append(arr[-1])

    # If current sum becomes negative, reset it to 0
    if curr_sum < 0:
      curr_sum = 0

    # If current sum is greater than max sum, update max sum
    max_sum = max(max_sum, curr_sum)

  return max_sum