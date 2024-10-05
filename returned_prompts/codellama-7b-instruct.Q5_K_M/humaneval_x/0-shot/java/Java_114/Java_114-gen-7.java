        int sum = 0;
        int min = Integer.MAX_VALUE;
        for (int i = 0; i < nums.size(); i++) {
            sum += nums.get(i);
            if (sum < min) {
                min = sum;
            }
            if (sum < 0) {
                continue A;
            }
        }
        return min;
    }
}





