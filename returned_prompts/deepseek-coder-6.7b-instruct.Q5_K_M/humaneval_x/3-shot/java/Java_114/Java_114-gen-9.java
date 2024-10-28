        int minSum = Integer.MAX_VALUE;
        int curSum = 0;

        for (int num : nums) {
            curSum += num;
            if (curSum < minSum) {
                minSum = curSum;
            }
            curSum = Math.min(curSum, 0);
        }

        return minSum;
    }
}

