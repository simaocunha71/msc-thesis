        int sum = Integer.MAX_VALUE;
        int currentSum = 0;

        for (Integer num : nums) {
            currentSum = Math.min(currentSum + num, num);
            sum = Math.min(sum, currentSum);
        }

        return sum;
    }
}

