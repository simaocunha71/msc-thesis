        int min = Integer.MAX_VALUE;
        int sum = 0;
        for (int i = 0; i < nums.size(); i++) {
            sum += nums.get(i);
            min = Math.min(min, sum);
            if (sum < 0) {
                sum = 0;
            }
        }
        return min;
    }
}
