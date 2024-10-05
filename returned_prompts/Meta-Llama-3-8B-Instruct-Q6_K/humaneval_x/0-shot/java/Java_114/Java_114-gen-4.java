    public int minSubArraySum(List<Integer> nums) {
        int min = Integer.MAX_VALUE;
        int sum = 0;
        for (int num : nums) {
            sum += num;
            min = Math.min(min, sum);
            if (sum < 0) {
                sum = 0;
            }
        }
        return min;
    }