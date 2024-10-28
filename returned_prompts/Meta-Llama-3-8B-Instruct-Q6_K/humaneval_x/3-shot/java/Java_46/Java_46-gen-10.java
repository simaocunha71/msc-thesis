        if (n <= 4) {
            switch (n) {
                case 0:
                    return 0;
                case 1:
                    return 0;
                case 2:
                    return 2;
                case 3:
                    return 0;
                default:
                    return 0;
            }
        }

        int[] fib4_array = new int[n + 1];
        fib4_array[0] = 0;
        fib4_array[1] = 0;
        fib4_array[2] = 2;
        fib4_array[3] = 0;

        for (int i = 4; i <= n; i++) {
            fib4_array[i] = fib4_array[i - 1] + fib4_array[i - 2] + fib4_array[i - 3] + fib4_array[i - 4];
        }

        return fib4_array[n];
    }
}

