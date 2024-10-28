        if (n < 1) {
            return 0;
        }

        int count = 0;
        for (int i = 1; i <= 10; i++) {
            if (i == 1) {
                count += n;
            } else {
                count += (int) Math.pow(10, n - 1);
            }
        }
        return count;
    }
}

