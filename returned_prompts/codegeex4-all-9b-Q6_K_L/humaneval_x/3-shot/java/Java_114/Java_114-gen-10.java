        int min_sum = Integer.MAX_VALUE;
        for (int i = 0; i < nums.size(); i++) {
            int current_sum = 0;
            for (int j = i; j < nums.size(); j++) {
                current_sum += nums.get(j);
                min_sum = Math.min(min_sum, current_sum);
            }
        }
        return min_sum;
    }
}

