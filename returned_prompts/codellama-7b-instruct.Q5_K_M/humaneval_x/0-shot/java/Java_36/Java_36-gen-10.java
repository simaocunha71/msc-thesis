        int cnt = 0;
        for (int i = 11; i < n; i += 11) {
            if (i % 13 == 0) {
                cnt++;
            }
        }
        return cnt;
    }
}
