        if (n > m) return -1;

        int total = (m - n + 1) * (n + m) / 2;
        int average = total / (m - n + 1);
        return Integer.toBinaryString(average);
    }
}


