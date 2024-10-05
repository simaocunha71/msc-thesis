        for (int i = 2; i < 10; i++) {
            if (a % i == 0) {
                int j = a / i;
                for (int k = 2; k < 10; k++) {
                    if (j % k == 0) {
                        int l = j / k;
                        if (l == 1) {
                            return true;
                        }
                    }
                }
            }
        }
        return false;
    }
}

