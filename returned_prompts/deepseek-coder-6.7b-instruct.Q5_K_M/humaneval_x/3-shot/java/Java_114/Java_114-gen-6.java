        int currentSum = nums.get(0);
        int minSum = nums.get(0);

        for(int i = 1; i < nums.size(); i++) {
            currentSum = Math.min(nums.get(i), currentSum + nums.get(i));
            minSum = Math.min(minSum, currentSum);
        }

        return minSum;
    }
}

