        if (n < 4) {
            return n == 3 ? 1 : n;
        }

        int[] fib4Sequence = new int[n+1];
        fib4Sequence[0] = 0;
        fib4Sequence[1] = 0;
        fib4Sequence[2] = 2;
        fib4Sequence[3] = 0;

        for (int i = 4; i <= n; i++) {
            fib4Sequence[i] = fib4Sequence[i-1] + fib4Sequence[i-2] + fib4Sequence[i-3] + fib4Sequence[i-4];
        }

        return fib4Sequence[n];
    }
}

This solution uses a dynamic programming approach to store the computed values in an array, which eliminates the need for recursion and allows it to compute the nth element of the fib4 sequence in O(n) time.
*/


/*
