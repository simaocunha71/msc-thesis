        return powerMod(2, n, p);
    }

    private int powerMod(int a, int b, int m) {
        if (b == 0) return 1;
        int p = powerMod(a, b / 2, m);
        p = (p * p) % m;
        if (b % 2 != 0) p = (p * a) % m;
        return p;
    }
}

