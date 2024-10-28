        for (int i = 1; i <= n; i++) {
            if (n % i == 0) {
                return i;
            }
        }
        return -1;
    }
}

