        int count = 0;
        for (int i = 1; i < 10; i++) {
            if (i == 1 || i % 10 == 1) {
                count++;
            }
        }
        return count * (int) Math.pow(9, n - 1);
    }
}

