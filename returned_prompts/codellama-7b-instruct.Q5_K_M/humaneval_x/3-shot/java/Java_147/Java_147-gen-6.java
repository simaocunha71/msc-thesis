        int count = 0;
        int[] nums = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            nums[i] = i * i - i + 1;
        }

        for (int i = 1; i <= n; i++) {
            for (int j = i + 1; j <= n; j++) {
                for (int k = j + 1; k <= n; k++) {
                    if (nums[i] + nums[j] + nums[k] % 3 == 0) {
                        count++;
                    }
                }
            }
        }
        return count;
    }
}

