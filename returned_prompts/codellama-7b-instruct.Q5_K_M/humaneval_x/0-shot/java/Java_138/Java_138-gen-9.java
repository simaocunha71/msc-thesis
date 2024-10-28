        for (int i = 2; i < 10000; i += 2) {
            for (int j = 2; j < 10000; j += 2) {
                for (int k = 2; k < 10000; k += 2) {
                    for (int l = 2; l < 10000; l += 2) {
                        if (i + j + k + l == n) {
                            return true;
                        }
                    }
                }
            }
        }
        return false;
    }
}











