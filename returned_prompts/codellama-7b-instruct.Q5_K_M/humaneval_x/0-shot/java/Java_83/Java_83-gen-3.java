        int count = 0;
        for (int i = 1; i <= 9; i++) {
            if (i == 1) {
                count += n - 1;
            } else if (i == 9) {
                count += n - 1;
            } else {
                count += n;
            }
        }
        return count;
    }
}