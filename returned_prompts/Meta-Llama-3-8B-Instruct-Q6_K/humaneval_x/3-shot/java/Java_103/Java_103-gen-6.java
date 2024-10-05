        if (n > m) return -1;

        double sum = 0.0;
        for (int i = n; i <= m; i++) {
            sum += i;
        }
        double avg = sum / (m - n + 1);
        int rounded_avg = (int) Math.round(avg);

        return Integer.toBinaryString(rounded_avg);
    }
}

