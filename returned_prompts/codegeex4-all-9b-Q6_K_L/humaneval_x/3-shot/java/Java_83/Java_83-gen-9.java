        if (n == 1) return 1;

        int count = 1;
        for (int i = 2; i <= n; i++) {
            count *= 10;
        }
        return 2 * count;
    }
}

