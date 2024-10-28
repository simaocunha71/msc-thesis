        for (int i = 2; i <= n; i += 2) {
            if (n - i < 0) return false;
            n -= i;
        }
        return n == 0;
    }
}

