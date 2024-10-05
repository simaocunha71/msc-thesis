        int count = 0;
        for (int i = 1; i < 10; i++) {
            count += Math.pow(9, n - 1);
        }
        for (int i = 1; i < 10; i++) {
            if (i == 1) {
                count++;
            } else {
                count += Math.pow(9, n - 1);
            }
        }
        return count;
    }
}

