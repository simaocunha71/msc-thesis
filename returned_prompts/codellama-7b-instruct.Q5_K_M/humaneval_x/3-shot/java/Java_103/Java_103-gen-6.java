        if (n > m) return -1;
        else {
            int sum = 0;
            for (int i = n; i <= m; i++) sum += i;
            double avg = sum / (m - n + 1);
            return Integer.toBinaryString(Math.round(avg));
        }
    }
}

