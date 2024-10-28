        if (n > m) return -1;

        int sum = 0;
        for (int i = n; i <= m; i++) sum += i;
        double avg = (double) sum / (m - n + 1);
        int rounded_avg = (int) Math.round(avg);
        String result = Integer.toBinaryString(rounded_avg);
        return result;
    }
}

