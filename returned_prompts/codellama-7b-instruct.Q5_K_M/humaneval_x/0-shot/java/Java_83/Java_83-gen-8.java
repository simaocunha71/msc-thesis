        if (n < 1) return 0;
        int cnt = 0;
        for (int i = 1; i <= n; i++) {
            int c = 10;
            int j = i;
            while (j-- > 0) {
                if (c % 10 == 0) break A;
                c /= 10;
            }
            cnt++;
        }
        return cnt;
    }
}




