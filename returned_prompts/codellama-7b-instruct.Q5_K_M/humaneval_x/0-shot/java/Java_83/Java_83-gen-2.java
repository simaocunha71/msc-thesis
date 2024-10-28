        int count = 0;
        int start = 1;
        int end = 1;

        for (int i = 1; i <= n - 1; i++) {
            start = start * 10;
            end = end * 10;
        }

        for (int i = start; i <= end; i++) {
            if (i % 10 == 1) {
                count++;
            }
        }

        return count;
    }
}
