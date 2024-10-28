        if (n > m) return -1;
        int total = 0;
        for (int i = n; i <= m; i++) {
            total += i;
        }
        int avg = total / (m - n + 1);
        return Integer.toBinaryString(avg);
    }
}

