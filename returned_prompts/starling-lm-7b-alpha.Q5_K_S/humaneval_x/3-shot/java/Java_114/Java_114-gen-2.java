        int result = Integer.MAX_VALUE;
        int current_sum = 0;
        for (int i = 0; i < nums.size(); i++) {
            current_sum += nums.get(i);
            int left = i;
            int right = i;
            while (current_sum > 0 && left > 0) {
                left -= 1;
                current_sum += nums.get(left);
            }
            while (current_sum > 0 && right + 1 < nums.size()) {
                right += 1;
                current_sum += nums.get(right);
            }
            result = Math.min(result, current_sum);
            current_sum = Math.max(current_sum, 0);
        }
        return result;
    }
}


```