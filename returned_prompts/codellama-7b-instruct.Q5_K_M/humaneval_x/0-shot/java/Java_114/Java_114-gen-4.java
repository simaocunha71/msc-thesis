        int min = 0;
        int sum = 0;
        int start = 0;
        for (int i = 0; i < nums.size(); i++) {
            sum += nums.get(i);
            if (sum < min) {
                min = sum;
            }
            if (sum < 0) {
                sum = 0;
                start++;
            }
        }
        return min;
    }
}
