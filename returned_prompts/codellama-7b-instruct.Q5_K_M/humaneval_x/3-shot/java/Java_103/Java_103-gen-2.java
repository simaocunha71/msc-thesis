        if (n > m) return -1;
        double avg = (n + m) / 2.0;
        int rounded_avg = (int) Math.round(avg);
        return Integer.toBinaryString(rounded_avg);
    }
}

