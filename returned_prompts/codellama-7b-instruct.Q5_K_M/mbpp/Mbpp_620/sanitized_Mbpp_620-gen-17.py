def largest_subset(nums: list) -> int:
  # Sort the list in descending order.
  nums.sort(reverse=True)

  # Initialize two pointers for the start and end of the subset.
  start = 0
  end = 0

  # Initialize the maximum size of the subset.
  max_size = 0

  # Loop through the list.
  while end < len(nums):
    # If the number at the end of the subset is divisible by the number at the start of the subset, increment the end pointer.
    if nums[end] % nums[start] == 0:
      end += 1

    # Otherwise, increment the start pointer.
    else:
      start += 1

    # Update the maximum size of the subset.
    max_size = max(max_size, end - start)

  # Return the maximum size of the subset.
  return max_size + 1