        for (int i = 2; i <= n; i += 2) {
            for (int j = 2; j <= n; j += 2) {
                for (int k = 2; k <= n; k += 2) {
                    for (int l = 2; l <= n; l += 2) {
                        if (i + j + k + l == n) return true;
                    }
                }
            }
        }
        return false;
    }
}

