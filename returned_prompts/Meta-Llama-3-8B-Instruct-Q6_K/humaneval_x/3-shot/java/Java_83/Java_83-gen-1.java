        int count = 0;
        for (int i = 1; i < 10; i++) {
            count += 1;
        }

        for (int i = 1; i < 10; i++) {
            for (int j = 0; j < n - 1; j++) {
                count += 1;
            }
        }

        return count;
    }
}

