        if (n > m) return -1;
        int avg = (int) Math.round((double) (m + n) / 2);
        return Integer.toBinaryString(avg);
    }
}

