        int minSum = Integer.MAX_VALUE;
        int currentSum = 0;

        for (int num : nums) {
            currentSum = Math.min(currentSum + num, num);
            minSum = Math.min(minSum, currentSum);
        }

        return minSum;
    }
}

