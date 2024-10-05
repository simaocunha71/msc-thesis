        if (n > m) return -1;
        int total = 0;
        for (int i = n; i <= m; i++) total += i;
        double avg = total / (m - n + 1);
        int avg_rounded = (int) Math.round(avg);
        String avg_bin = Integer.toBinaryString(avg_rounded);
        return avg_bin;
    }
}

