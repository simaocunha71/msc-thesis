        int[] fibfib_array = new int[n + 1];
        fibfib_array[0] = 0;
        fibfib_array[1] = 0;
        fibfib_array[2] = 1;

        for (int i = 3; i <= n; i++) {
            fibfib_array[i] = fibfib_array[i - 1] + fibfib_array[i - 2] + fibfib_array[i - 3];
        }

        return fibfib_array[n];
    }
}

