        int result = Integer.MAX_VALUE;
        int current_sum = 0;
        for (int num : nums) {
            current_sum += num;
            result = Math.min(result, current_sum);
            if (current_sum < 0) current_sum = 0;
        }
        return result;
    }
}

