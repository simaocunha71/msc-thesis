        int min_sum = Integer.MAX_VALUE;
        int current_sum = 0;

        for (int i = 0; i < nums.size(); i++) {
            current_sum += nums.get(i);
            min_sum = Math.min(min_sum, current_sum);

            while (current_sum > 0 && i < nums.size() - 1 && current_sum > nums.get(i + 1)) {
                current_sum -= nums.get(i + 1);
                min_sum = Math.min(min_sum, current_sum);
                i += 1;
            }
        }
        return min_sum;
    }
}

