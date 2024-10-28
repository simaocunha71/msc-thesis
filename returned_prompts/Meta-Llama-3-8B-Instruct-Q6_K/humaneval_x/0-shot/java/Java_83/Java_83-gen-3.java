        int count = 0;
        for (int i = 1; i < 10; i++) {
            for (int j = 0; j < n; j++) {
                if ((i == 1 && j == 0) || (i == 1 && j == n - 1)) {
                    count++;
                }
            }
        }
        return count;
    }
}
