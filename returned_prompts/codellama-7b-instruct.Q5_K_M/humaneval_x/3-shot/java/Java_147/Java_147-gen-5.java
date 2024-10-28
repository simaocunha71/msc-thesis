        int result = 0;
        int[] numbers = new int[n];
        for (int i = 0; i < n; i++) {
            numbers[i] = i * i - i + 1;
        }
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                for (int k = j + 1; k < n; k++) {
                    if (numbers[i] + numbers[j] + numbers[k] % 3 == 0) {
                        result++;
                    }
                }
            }
        }
        return result;
    }
}

