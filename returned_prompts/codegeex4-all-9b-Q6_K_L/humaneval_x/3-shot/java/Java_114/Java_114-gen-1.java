        int result = Integer.MAX_VALUE;
        int current_sum = 0;

        for (int i = 0; i < nums.size(); i++) {
            current_sum += nums.get(i);

            result = Math.min(result, current_sum);
            current_sum = Math.max(current_sum, 0);
        }
        return result;
    }
}

