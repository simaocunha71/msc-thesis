

    public int fibfib(int n) {
        if (n <= 1) {
            return 0;
        } else if (n == 2) {
            return 1;
        } else {
            int[] fibfib = new int[n + 1];
            fibfib[1] = 0;
            fibfib[2] = 1;
            for (int i = 3; i <= n; i++) {
                fibfib[i] = fibfib[i - 1] + fib