        int min_sum = Integer.MAX_VALUE;
        int current_sum = 0;

        for (int num : nums) {
            current_sum += num;
            min_sum = Math.min(min_sum, current_sum);
            if (current_sum < 0) current_sum = 0;
        }
        return min_sum;
    }
}

