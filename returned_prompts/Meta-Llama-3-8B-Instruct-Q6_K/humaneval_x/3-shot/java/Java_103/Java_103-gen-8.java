        if (n > m) {
            return -1;
        }

        int sum = 0;
        for (int i = n; i <= m; i++) {
            sum += i;
        }

        double avg = (double) sum / (m - n + 1);
        avg = Math.round(avg);

        String binary = Integer.toBinaryString((int) avg);
        return binary;
    }
}

