        if (n <= 3) {
            return 0;
        }
        if (n == 4) {
            return 2;
        }
        int[] result = new int[n + 1];
        result[0] = 0;
        result[1] = 0;
        result[2] = 2;
        result[3] = 0;

        for (int i = 4; i <= n; i++) {
            result[i] = result[i - 1] + result[i - 2] + result[i - 3] + result[i - 4];
        }
        return result[n];
    }
}

