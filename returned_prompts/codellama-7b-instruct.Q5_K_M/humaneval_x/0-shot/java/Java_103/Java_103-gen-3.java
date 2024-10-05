        if (n > m) {
            return -1;
        }
        long sum = 0;
        for (int i = n; i <= m; i++) {
            sum += i;
        }
        long avg = sum / (m - n + 1);
        return Integer.toBinaryString((int) avg);
    }
}
