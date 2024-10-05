        if (n > m) return -1;

        int rounded = (int) Math.round((double) (n + m) / 2);
        return Integer.toBinaryString(rounded);
    }
}

