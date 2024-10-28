        if (n > m) return -1;
        double average = (double) (n + m) / 2;
        long rounded = Math.round(average);
        return Integer.toBinaryString(rounded);
    }
}

