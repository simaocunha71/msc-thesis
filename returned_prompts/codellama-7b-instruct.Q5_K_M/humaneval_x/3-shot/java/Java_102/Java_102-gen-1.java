        if (x % 2 == 0) {
            for (int i = x; i <= y; i++) {
                if (i % 2 == 0) {
                    return i;
                }
            }
        }

        for (int i = x + 1; i <= y; i++) {
            if (i % 2 == 0) {
                return i;
            }
        }

        return -1;
    }
}

