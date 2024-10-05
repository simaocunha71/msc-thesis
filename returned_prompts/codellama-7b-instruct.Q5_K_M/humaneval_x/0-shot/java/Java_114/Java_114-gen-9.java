        int sum = 0;
        for (int i = 0; i < nums.size(); i++) {
            sum = sum + nums.get(i);
            if (sum < 0) {
                sum = 0;
            }
        }
        return sum;
    }
}
