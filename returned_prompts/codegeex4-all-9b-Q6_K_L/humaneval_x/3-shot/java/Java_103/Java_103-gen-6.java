        if (n > m) {
            return -1;
        }
        int total = 0;
        for (int i = n; i <= m; i++) {
            total += i;
        }
        int rounded = Math.round(total / (double) (m - n + 1));
        return Integer.toBinaryString(rounded);
    }
}

