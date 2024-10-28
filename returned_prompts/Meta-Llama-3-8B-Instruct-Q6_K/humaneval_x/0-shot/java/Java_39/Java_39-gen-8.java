        int[] fib = new int[n+1];
        fib[0] = 0;
        fib[1] = 1;
        for(int i = 2; i <= n; i++) {
            fib[i] = fib[i-1] + fib[i-2];
        }
        for(int i = 0; i <= n; i++) {
            if(isPrime(fib[i])) {
                return fib[i];
            }
        }
        return -1;
    }

    public boolean isPrime(int num) {
        if(num < 2) {
            return false;
        }
        for(int i = 2; i * i <= num; i++) {
            if(num % i == 0) {
                return false;
            }
        }
        return true;
    }
}
