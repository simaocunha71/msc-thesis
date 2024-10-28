        if (n == 0) return 0;
        if (n == 1) return 0;
        if (n == 2) return 1;

        int[] fibfib = new int[n+1];
        fibfib[0] = 0;
        fibfib[1] = 0;
        fibfib[2] = 1;

        for (int i = 3; i <= n; i++) {
            fibfib[i] = fibfib[i-1] + fibfib[i-2] + fibfib[i-3];
        }

        return fibfib[n];
    }
}

