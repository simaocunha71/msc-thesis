        if (n > m) {
            return -1;
        }
        int sum = 0;
        for (int i = n; i <= m; i++) {
            sum += i;
        }
        double average = (double) sum / (m - n + 1);
        int rounded = (int) Math.round(average);
        return Integer.toBinaryString(rounded);
    }
}

