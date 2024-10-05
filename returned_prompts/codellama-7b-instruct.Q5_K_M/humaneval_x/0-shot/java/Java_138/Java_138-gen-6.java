        if (n < 8) {
            return false;
        }
        for (int i = 2; i <= 8; i += 2) {
            for (int j = 2; j <= 8; j += 2) {
                for (int k = 2; k <= 8; k += 2) {
                    for (int l = 2; l <= 8; l += 2) {
                        if (n == i + j + k + l) {
                            return true;
                        }
                    }
                }
            }
        }
        return false;
    }
}
