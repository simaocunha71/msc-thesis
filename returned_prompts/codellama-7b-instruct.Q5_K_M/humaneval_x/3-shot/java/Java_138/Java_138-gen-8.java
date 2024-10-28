        for (int i = 0; i < 100; i++) {
            for (int j = i + 1; j < 100; j++) {
                for (int k = j + 1; k < 100; k++) {
                    for (int l = k + 1; l < 100; l++) {
                        if (i + j + k + l == n) {
                            if (i % 2 == 0 && j % 2 == 0 && k % 2 == 0 && l % 2 == 0) {
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

