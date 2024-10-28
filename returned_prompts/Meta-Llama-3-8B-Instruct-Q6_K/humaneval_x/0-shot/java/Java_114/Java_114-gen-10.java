    public int minSubArraySum(List<Integer> nums) {
        if (nums.isEmpty()) {
            throw new RuntimeException("Input array is empty");
        }
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
    }
}