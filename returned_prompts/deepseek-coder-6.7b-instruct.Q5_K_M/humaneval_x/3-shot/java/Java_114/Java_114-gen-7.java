        int minSum = Integer.MAX_VALUE, currentSum = 0;
        for(int num : nums) {
            currentSum += num;
            minSum = Math.min(minSum, currentSum);
            currentSum = Math.min(currentSum, 0);
        }
        return minSum;
    }
}

