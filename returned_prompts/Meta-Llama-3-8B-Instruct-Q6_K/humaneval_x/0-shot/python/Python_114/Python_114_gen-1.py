
In this solution, we initialize `min_sum` to positive infinity and `current_sum` to 0. Then, we iterate over the input array `nums`. For each number, we add it to `current_sum` and update `min_sum` if `current_sum` is smaller. If `current_sum` becomes positive, we reset it to 0. Finally, we return `min_sum` as the minimum sum of any non-empty sub-array.

For example, for the input `[2, 3, 4, 1, 2, 4]`, the function will return `1` because the minimum sum of any non-empty sub-array is `1` (for the sub-array `[1]`).

For the input `[-1, -2, -3]`, the function will return `-6` because the minimum sum of any non-empty sub-array is `-6` (for the sub-array `[-1, -2, -3]`).

This solution has a time complexity of O(n), where n is the length of the input array, because we iterate over the array once. The space complexity is O(1), because we use a constant amount of space to store `min_sum` and `current_sum`.