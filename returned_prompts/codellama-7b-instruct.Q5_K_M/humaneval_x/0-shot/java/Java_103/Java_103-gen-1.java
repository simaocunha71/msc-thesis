        if (n > m) {
            return -1;
        }
        int sum = 0;
        int count = 0;

        for (int i = n; i <= m; i++) {
            sum += i;
            count++;
        }

        int avg = sum / count;
        int rounded = Math.round(avg);
        return Integer.toBinaryString(rounded);
    }
}

