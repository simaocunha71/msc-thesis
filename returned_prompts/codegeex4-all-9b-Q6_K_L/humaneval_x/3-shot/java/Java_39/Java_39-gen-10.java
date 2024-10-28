        int fib = 1, prev_fib = 0, fib_index = 1;
        while (fib_index < n) {
            int temp = fib;
            fib += prev_fib;
            prev_fib = temp;
            fib_index += 1;
        }

        while (true) {
            if (isPrime(fib)) return fib;
            int temp = fib;
            fib += prev_fib;
            prev_fib = temp;
        }

        // dummy return, just to satisfy compiler
        return 0;
    }

    public boolean isPrime(int num) {
        if (num < 2) return false;
        for (int i = 2; i <= Math.sqrt(num); i += 1) {
            if (num % i == 0) return false;
        }
        return true;
    }
}

