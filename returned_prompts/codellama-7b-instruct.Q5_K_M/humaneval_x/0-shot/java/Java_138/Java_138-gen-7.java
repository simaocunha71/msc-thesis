        for (int i = 1; i <= 100; i++) {
            if (i % 2 == 0) {
                for (int j = 1; j <= 100; j++) {
                    if (j % 2 == 0) {
                        if (i + j == n) {
                            return true;
                        }
                    }
                }
            }
        }
        return false;
    }
}

