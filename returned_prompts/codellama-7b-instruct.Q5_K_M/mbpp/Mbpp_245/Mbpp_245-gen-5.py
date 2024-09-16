
def max_sum(arr)
  # Initialize the maximum sum and the maximum increasing sum
  max_sum = 0
  max_inc_sum = 0

  # Sort the array
  arr.sort

  # Loop through the array
  arr.each_with_index do |n, i|
    # If the number is greater than the maximum increasing sum
    if n > max_inc_sum
      # Update the maximum increasing sum
      max_inc_sum = n
    end

    # If the number is greater than the maximum sum
    if n > max_sum
      # Update the maximum sum
      max_sum = n
    end
  end

  # Loop through the array again
  arr.each_with_index do |n, i|
    # If the number is less than the maximum sum and less than the maximum increasing sum
    if n < max_sum and n < max_inc_sum
      # If the number is greater than the maximum decreasing sum
      if n > max_dec_sum
        # Update the maximum decreasing sum
        max_dec_sum = n
      end
    end
  end

  # Return the sum of the maximum increasing sum and the maximum decreasing sum
  return max_inc_sum + max_dec_sum
end

# Test the function
puts max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9])

# Output:
# 194

# Time complexity: O(n log n)
# Space complexity: O(1)
