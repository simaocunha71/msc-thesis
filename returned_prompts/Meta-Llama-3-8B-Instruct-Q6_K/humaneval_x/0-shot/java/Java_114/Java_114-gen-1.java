public int minSubArraySum(List<Integer> nums) {
    int minSum = Integer.MAX_VALUE;
    int currentSum = 0;
    for (int num : nums) {
        currentSum += num;
        minSum = Math.min(minSum, currentSum);
        if (currentSum < 0) {
            currentSum = 0;
        }
    }
    return minSum;
}
