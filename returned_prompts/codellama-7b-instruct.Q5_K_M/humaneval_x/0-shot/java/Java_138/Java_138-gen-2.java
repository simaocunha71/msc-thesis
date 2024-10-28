        for (int i = 0; i < 10000; i++) {
            int j = i + 2;
            int k = j + 2;
            int l = k + 2;
            if (n == i + j + k + l) {
                return true;
            }
        }
        return false;
    }
}
