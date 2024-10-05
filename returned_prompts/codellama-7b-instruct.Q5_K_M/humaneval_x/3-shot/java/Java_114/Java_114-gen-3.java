        int min_sum = Integer.MAX_VALUE;
        int current_sum = 0;

        for (int i = 0; i < nums.size(); i++) {
            current_sum += nums.get(i);
            if (current_sum < min_sum) min_sum = current_sum;

            if (current_sum > 0) current_sum = 0;
        }
        return min_sum;
    }
}

