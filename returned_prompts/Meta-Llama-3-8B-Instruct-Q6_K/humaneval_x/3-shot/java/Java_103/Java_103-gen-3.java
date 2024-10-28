        if (n > m) {
            return -1;
        }
        double sum = 0;
        for (int i = n; i <= m; i++) {
            sum += i;
        }
        double avg = Math.round(sum / (m - n + 1));
        return Integer.toBinaryString((int) avg);
    }
}

