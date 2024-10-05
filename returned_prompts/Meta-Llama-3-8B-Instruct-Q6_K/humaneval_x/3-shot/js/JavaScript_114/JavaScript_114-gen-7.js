  let min_sum = Infinity;
  for (let i = 0; i < nums.length; i++) {
    let current_sum = 0;
    for (let j = i; j < nums.length; j++) {
      current_sum += nums[j];
      min_sum = Math.min(min_sum, current_sum);
    }
  }
  return min_sum;
} // Note: This function has a time complexity of O(n^2), which may not be efficient for large inputs. A more efficient solution could be achieved with a single pass through the array and a running sum, which would have a time complexity of O(n).