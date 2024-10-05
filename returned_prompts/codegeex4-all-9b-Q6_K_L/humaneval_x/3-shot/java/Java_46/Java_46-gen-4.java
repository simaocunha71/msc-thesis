        int[] fibs = new int[n+1];
        fibs[0] = 0;
        fibs[1] = 0;
        fibs[2] = 2;
        fibs[3] = 0;

        for (int i = 4; i <= n; i++) {
            fibs[i] = fibs[i-1] + fibs[i-2] + fibs[i-3] + fibs[i-4];
        }

        return fibs[n];
    }
}

