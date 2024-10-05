    public int minSubArraySum(List<Integer> nums) {
        int minSum = Integer.MAX_VALUE;
        int currentSum = 0;
        for (int num : nums) {
            currentSum += num;
            minSum = Math.min(minSum, currentSum);
            if (currentSum > 0) {
                currentSum = 0;
            }
        }
        return minSum;
    }  // This function calculates the minimum sum of any non-empty sub-array of the given array. It initializes two variables, minSum and currentSum, to keep track of the minimum sum and the sum of the current sub-array, respectively. It then iterates over the array, adding each element to the currentSum and updating the minSum if necessary. If the currentSum becomes positive, it resets the currentSum to 0 to ensure that it only includes non-empty sub-arrays. Finally, it returns the minimum sum.  // Time complexity: O(n), where n is the size of the input array.  // Space complexity: O(1), as it only uses a constant amount of space.  // Example: minSubArraySum(Arrays.asList(2, 3, 4, 1, 2, 4)) == 1  // Explanation: The minimum sum of any non-empty sub-array is 1, which is obtained by the sub-array [1].  // Example: minSubArraySum(Arrays.asList(-1, -2, -3)) == -6  // Explanation: The minimum sum of any non-empty sub-array is -6, which is obtained by the sub-array [-1, -2, -3].  // Example: minSubArraySum(Arrays.asList(1, -2, 3)) == -2  // Explanation: The minimum sum of any non-empty sub-array is -2, which is obtained by the sub-array [-2].  // Example: minSubArraySum(Arrays.asList(1, 2, 3, 4, 5)) == 1  // Explanation: The minimum sum of any non-empty sub-array is 1, which is obtained by the sub-array [1].  // Example: minSubArraySum(Arrays.asList(-1, -2, -3, -4, -5)) == -5  // Explanation: The minimum sum of any non-empty sub-array is -5, which is obtained by the sub-array [-5].  // Example: minSubArraySum(Arrays.asList(1