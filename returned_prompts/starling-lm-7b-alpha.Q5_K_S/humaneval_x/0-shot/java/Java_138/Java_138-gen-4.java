        if (n == 0 || n < 0) {
            return false;
        }
        if (n % 2 != 0) {
            return false;
        }
        if (n == 2) {
            return true;
        }
        if (n == 4) {
            return false;
        }
        if (n == 6) {
            return false;
        }

        for (int i = 2; i < n / 2 + 1; i++) {
            if (n - i <= 0) {
                break A;
            }
            if (n - i >= 0 && n - i % 2 == 0) {
                for (int j = 2; j < (n - i) / 2 + 1; j++) {
                    if ((n - i - j) % 2 == 0 && (n - i - j) >= 0) {
                        for (int k = 2; k < (n - i - j) / 2 + 1; k++) {
                            if ((n - i - j - k) % 2 == 0 && (n - i - j - k) >= 0) {
                                return true;
                            }
                        }
                    }
                }
            }
        }
        return false;
    }
}


























































































































































































