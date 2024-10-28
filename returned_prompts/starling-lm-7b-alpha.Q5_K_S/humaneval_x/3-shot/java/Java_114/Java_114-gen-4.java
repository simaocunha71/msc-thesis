        int result = Integer.MAX_VALUE;
        int total_sum = 0;
        int start_index = 0;
        for (int i = 0; i < nums.size(); i++) {
            total_sum += nums.get(i);
            while (total_sum < 0) {
                total_sum -= nums.get(start_index);
                start_index += 1;
            }
            result = Math.min(result, total_sum);
        }
        return result;
    }
}

