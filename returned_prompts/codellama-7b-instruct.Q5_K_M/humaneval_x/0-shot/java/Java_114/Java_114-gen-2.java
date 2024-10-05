        int minSum = 0;
        int sum = 0;
        for (Integer num : nums) {
            sum += num;
            minSum = Math.min(minSum, sum);
            if (sum < 0) {
                sum = 0;
            }
        }
        return minSum;
    }
}





