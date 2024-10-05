        if (n < 1) {
            return 0;
        }

        if (n == 1) {
            return 1;
        }

        int count = 1;
        for (int i = 0; i < n - 2; i++) {
            count *= 10;
        }

        return 2 * count;
    }
}

