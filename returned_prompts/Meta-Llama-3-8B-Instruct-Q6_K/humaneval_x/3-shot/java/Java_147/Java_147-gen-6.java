        int count = 0;
        for (int i = 1; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int a = i * i - i + 1;
                int b = j * j - j + 1;
                for (int k = j + 1; k <= n; k++) {
                    int c = k * k - k + 1;
                    if ((a + b + c) % 3 == 0) {
                        count++;
                    }
                }
            }
        }
        return count;
    }
}

