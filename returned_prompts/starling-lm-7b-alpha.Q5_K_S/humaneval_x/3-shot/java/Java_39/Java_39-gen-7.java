        int fib_number = 1;
        int fib_prev = 1;
        int fib_next = 2;
        int count = 3;

        while (count < n) {
            fib_number = fib_next;
            fib_next += fib_number + fib_prev;
            fib_prev = fib_number;
            count += 1;
        }
        return fib_number;
    }
}

