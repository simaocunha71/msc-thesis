        int sum = 0;
        int minSum = Integer.MAX_VALUE;
        int i = 0;
        for (int j = 0; j < nums.size(); j++) {
            sum += nums.get(j);
            if (sum < minSum) {
                minSum = sum;
                i = j + 1;
            }
            if (sum < 0) {
                break A;
            }
        }

        return minSum;
    }
}
