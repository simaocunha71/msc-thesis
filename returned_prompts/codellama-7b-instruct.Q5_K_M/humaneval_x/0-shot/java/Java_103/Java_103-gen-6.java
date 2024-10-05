        int average = 0;
        int count = 0;
        for (int i = n; i <= m; i++) {
            average += i;
            count++;
        }
        if (n > m) return -1;
        average = average / count;
        return Integer.toBinaryString(Math.round(average));
    }
}
