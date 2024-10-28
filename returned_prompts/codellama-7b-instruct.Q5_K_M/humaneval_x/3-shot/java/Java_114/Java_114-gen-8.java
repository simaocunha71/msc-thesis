        int sum = 0;
        int min_sum = Integer.MAX_VALUE;

        for (int i = 0; i < nums.size(); i++) {
            sum += nums.get(i);
            min_sum = Math.min(min_sum, sum);

            if (sum < 0) {
                sum = 0;
            }
        }
        return min_sum;
    }
}

