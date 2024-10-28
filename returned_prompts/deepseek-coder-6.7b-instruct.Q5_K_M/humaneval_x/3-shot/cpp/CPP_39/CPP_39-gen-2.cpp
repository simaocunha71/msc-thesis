    int fib1 = 0, fib2 = 1, fib3 = 1;
    int count = 0;
    bool isPrime;

    while (count < n) {
        fib1 = fib2;
        fib2 = fib3;
        fib3 = fib1 + fib2;

        isPrime = true;
        if (fib2 < 2)
            isPrime = false;
        for (int i = 2; i * i <= fib2; ++i) {
            if (fib2 % i == 0) {
                isPrime = false;
                break;
            }
        }
        if (isPrime)
            ++count;
    }

    return fib2;
}

