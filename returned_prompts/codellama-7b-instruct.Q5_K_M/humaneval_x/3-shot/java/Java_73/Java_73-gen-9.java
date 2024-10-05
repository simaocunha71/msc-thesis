        int[] arr_int = new int[arr.size()];
        for (int i = 0; i < arr.size(); i++) {
            arr_int[i] = arr.get(i);
        }

        int max = 0;
        for (int i = 0; i < arr.size(); i++) {
            if (arr_int[i] > max) {
                max = arr_int[i];
            }
        }

        int[] dp = new int[max + 1];
        for (int i = 0; i < dp.length; i++) {
            dp[i] = max;
        }
        for (int i = 0; i < arr_int.length; i++) {
            dp[arr_int[i]] = Math.min(dp[arr_int[i]], dp[arr_int[i] - 1] + 1);
        }
        int min_change = dp[max];
        return min_change;
    }
}

