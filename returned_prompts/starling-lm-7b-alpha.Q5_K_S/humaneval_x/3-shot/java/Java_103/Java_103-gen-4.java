        if (n > m) return -1;

        int sum = 0;
        for (int i = n; i <= m; i++) {
            sum += i;
        }
        double avg = sum / (m - n + 1);
        int rounded = (int) Math.round(avg);
        return Integer.toBinaryString(rounded);
    }
}

