def maxAverageOfPath(arr: list):
  # Find the maximum average of all paths
  # from top-left to bottom-right.
  #
  # Example:
  # [[1, 2, 3],
  #  [6, 5, 4],
  #  [7, 3, 9]]
  #
  # The maximum average of all paths is (1 + 2 + 3 + 6 + 5 + 4 + 7 + 3 + 9) / 9 = 5.2

  # Initialize variables for rows and columns
  rows = len(arr)
  cols = len(arr[0])

  # Initialize variables for max_sum and count
  max_sum = 0
  count = 0

  # Loop through each row
  for i in range(rows):
    # Loop through each column
    for j in range(cols):
      # Initialize variables for current row and column
      current_row = i
      current_col = j

      # Initialize variable for current sum
      current_sum = 0

      # Loop through each cell in the path
      while current_row < rows and current_col < cols:
        # Add the current cell to the sum
        current_sum += arr[current_row][current_col]

        # Increment the count
        count += 1

        # Move down
        current_row += 1

        # If we're not at the end of the row, move right
        if current_row < rows:
          current_col += 1

      # If the sum is greater than the max sum, set the max sum and count
      if current_sum > max_sum:
        max_sum = current_sum
        count = 1
      # If the sum is equal to the max sum, increment the count
      elif current_sum == max_sum:
        count += 1

  # Return the average of the max sum and count
  return max_sum / count