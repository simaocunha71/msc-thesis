        if (n == 0) return 0;
        if (n == 1) return 0;
        if (n == 2) return 2;
        if (n == 3) return 0;

        int[] f = {0, 0, 2, 0};
        int i = 4;

        while (i <= n) {
            f[i & 3] = f[(i - 1) & 3] + f[(i - 2) & 3] + f[(i - 3) & 3] + f[(i - 4) & 3];
            i += 1;
        }

        return f[n & 3];
    }
}

