        int result = nums.get(0);
        for (int i = 0; i < nums.size(); i++) {
            int current_sum = 0;
            for (int j = i; j < nums.size(); j++) {
                current_sum += nums.get(j);
                result = Math.min(result, current_sum);
            }
        }
        return result;
    }
}

