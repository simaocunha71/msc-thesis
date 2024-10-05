        int result = Integer.MAX_VALUE;
        int current_sum = 0;
        for (int i = 0; i < nums.size(); i++) {
            current_sum += nums.get(i);
            result = Math.min(result, current_sum);
            while (i < nums.size() && current_sum > 0) {
                current_sum -= nums.get(i);
                i++;
            }
        }
        return result;
    }
}


