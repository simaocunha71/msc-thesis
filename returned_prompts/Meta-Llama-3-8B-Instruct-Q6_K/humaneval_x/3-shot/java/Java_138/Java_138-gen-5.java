        for (int i = 2; i < n; i++) {
            if (i % 2 == 0) {
                for (int j = 2; j < n; j++) {
                    if (j % 2 == 0) {
                        for (int k = 2; k < n; k++) {
                            if (k % 2 == 0) {
                                for (int l = 2; l < n; l++) {
 if (l % 2 == 0) {
 if (i + j + k + l == n) return true;
 }
                                }
                            }
                        }
                    }
                }
            }
        }
        return false;
    }
}

