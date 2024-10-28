        int[] fibfib = new int[n + 1];
        fibfib[0] = 0;
        fibfib[1] = 0;
        fibfib[2] = 1;
        for (int i = 3; i < fibfib.length; i++) {
            fibfib[i] = fibfib[i - 1] + fibfib[i - 2] + fibfib[i - 3];
        }
        return fibfib[n];
    }
}

