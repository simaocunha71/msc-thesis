        int[] result = new int[100];
        result[1] = 2;
        result[2] = 3;
        result[3] = 5;
        result[4] = 8;
        for (int i = 5; i <= n; i++) {
            result[i] = result[i - 1] + result[i - 2] + result[i - 3] + result[i - 4];
        }
        return result[n];
    }
}

