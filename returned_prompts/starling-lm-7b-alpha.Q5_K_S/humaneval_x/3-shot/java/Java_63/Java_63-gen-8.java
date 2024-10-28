        if (n <= 2) return 0;
        int[] result = new int[n + 1];
        result[0] = 0;
        result[1] = 0;
        result[2] = 1;
        for (int i = 3; i <= n; i++) {
            result[i] = result[i - 1] + result[i - 2] + result[i - 3];
        }
        return result[n];
    }
}





```