        int result = 0;
        for (int i = 0; i < n; i++) {
            int a = i * i - i + 1;
            for (int j = i + 1; j < n; j++) {
                int b = j * j - j + 1;
                for (int k = j + 1; k < n; k++) {
                    int c = k * k - k + 1;
                    if ((a + b + c) % 3 == 0) result += 1;
                }
            }
        }
        return result;
    }
}

