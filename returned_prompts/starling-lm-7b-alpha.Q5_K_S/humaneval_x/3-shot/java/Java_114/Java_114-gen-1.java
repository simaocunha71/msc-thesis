        int min_sum = Integer.MAX_VALUE;
        int current_sum = 0;
        for (int i = 0; i < nums.size(); i++) {
            current_sum += nums.get(i);
            for (int j = i + 1; j <= nums.size(); j++) {
                if (current_sum < min_sum) {
                    min_sum = current_sum;
                }
                if (j < nums.size()) {
                    current_sum += nums.get(j);
                } else {
                    break;
                }
            }
            current_sum = 0;
        }
        return min_sum;
    }
}


```