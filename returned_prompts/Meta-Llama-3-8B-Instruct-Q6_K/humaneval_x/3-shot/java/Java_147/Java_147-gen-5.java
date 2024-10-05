        int count = 0;
        for (int i = 1; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int k = j + 1;
                while (k < n) {
                    int sum = (i * i - i + 1) + (j * j - j + 1) + (k * k - k + 1);
                    if (sum % 3 == 0) {
                        count++;
                    }
                    k++;
                }
            }
        }
        return count;
    }
}

