        if (n <= 1) return 0;
        if (n == 2) return 1;
        int[] fibfib_values = new int[n+1];
        fibfib_values[1] = fibfib_values[2] = 0;
        fibfib_values[2] = 1;
        for (int i = 3; i <= n; i++) {
            fibfib_values[i] = fibfib_values[i-1] + fibfib_values[i-2] + fibfib_values[i-3];
        }
        return fibfib_values[n];
    }
}

