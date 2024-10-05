        if (n == 0 || n == 1) return 0;
        if (n == 2) return 2;
        if (n == 3) return 0;

        int[] fib_nums = new int[n + 1];
        fib_nums[0] = 0;
        fib_nums[1] = 0;
        fib_nums[2] = 2;
        fib_nums[3] = 0;

        for (int i = 4; i <= n; i++) {
            fib_nums[i] = fib_nums[i - 1] + fib_nums[i - 2] + fib_nums[i - 3] + fib_nums[i - 4];
        }
        return fib_nums[n];
    }
}

