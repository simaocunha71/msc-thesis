        if (n > m) return -1;

        int rounded_avg = Math.round((n + m) / 2.0f);
        return Integer.toBinaryString(rounded_avg);
    }
}

