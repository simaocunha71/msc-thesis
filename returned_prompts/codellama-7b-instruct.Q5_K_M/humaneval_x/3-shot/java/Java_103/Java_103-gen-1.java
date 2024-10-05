        if (n > m) return -1;

        int sum = 0;
        for (int i = n; i <= m; i++) {
            sum += i;
        }

        int avg = (int) Math.round(sum / (double) (m - n + 1));
        return String.format("%1$b", avg);

    }
}

