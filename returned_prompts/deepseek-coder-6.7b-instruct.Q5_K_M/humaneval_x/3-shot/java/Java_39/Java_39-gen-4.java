        int fib1 		= 0;
        int fib2 		= 1;
        int fibNext	= 0;
        int countPrime = 0;

        while (true) {
            fibNext = fib1 + fib2;
            fib1 = fib2;
            fib2 = fibNext;
            if (isPrime(fibNext)) {
            	countPrime++;
            }
            if (countPrime == n) {
            	return fibNext;
            }
        }
    }

    private boolean isPrime(int n) {
        if (n == 0 || n == 1) {
        	return false;
        }
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
            	return false;
            }
        }
        return true;
    }
}

