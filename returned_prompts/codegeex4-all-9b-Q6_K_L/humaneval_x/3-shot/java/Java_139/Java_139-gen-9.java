        long result = 1;
        for (int i = 1; i <= n; i++) {
            long temp = 1;
            for (int j = 1; j <= i; j++) {
                temp *= j;
            }
            result *= temp;
        }
        return result;

    }
}

