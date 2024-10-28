        int n = nums.size();
        int min = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            int sum = 0;
            for (int j = i; j < n; j++) {
                sum += nums.get(j);
                if (sum < min) {
                    min = sum;
                    break;
                }
            }
        }
        return min;
    }
}

