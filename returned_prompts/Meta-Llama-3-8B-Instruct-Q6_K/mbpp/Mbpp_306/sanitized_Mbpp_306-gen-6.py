def max_sum_increasing_subseq(lst, i, k, j):
  # Initialize the maximum sum
  max_sum = 0
  
  # Iterate from i to j
  for x in range(i, j):
    # If the current element is greater than the previous one, it's part of the increasing subsequence
    if x > i and lst[x] > lst[x - 1]:
      # Update the maximum sum
      max_sum += lst[x]
  
  # Return the maximum sum
  return max_sum