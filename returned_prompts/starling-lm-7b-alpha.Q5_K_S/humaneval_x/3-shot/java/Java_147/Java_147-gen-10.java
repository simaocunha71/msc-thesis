        int[] numbers = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            numbers[i] = (i * i) - i + 1;
        }
        int result = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = i + 1; j <= n; j++) {
                for (int k = j + 1; k <= n; k++) {
                    if ((numbers[i] + numbers[j] + numbers[k]) % 3 == 0) {
                        result += 1;
                    }
                }
            }
        }
        return result;
    }
}

