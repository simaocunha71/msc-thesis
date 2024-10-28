        if (n > m) {
            return -1;
        }
        double sum = 0.0;
        for (int i = n; i <= m; i++) {
            sum += i;
        }
        double average = sum / (m - n + 1);
        return Integer.toBinaryString(Math.round(average));
    }
}

