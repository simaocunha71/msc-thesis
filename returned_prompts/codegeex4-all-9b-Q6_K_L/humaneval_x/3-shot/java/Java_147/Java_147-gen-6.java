        int count = 0;
        for (int i = 0; i < n - 2; i++) {
            for (int j = i + 1; j < n - 1; j++) {
                for (int k = j + 1; k < n; k++) {
                    if ((i * i - i + 1 + j * j - j + 1 + k * k - k) % 3 == 0) {
                        count += 1;
                    }
                }
            }
        }
        return count;
    }
}

