        int count = 0;
        int i = 2;
        while(count < n){
            if(isPrime(i) && isFibonacci(i)){
                count++;
            }
            i++;
        }
        return i-1;
    }

    private boolean isPrime(int num){
        if(num < 2) return false;
        for(int i = 2; i*i <= num; i++){
            if(num % i == 0)
                return false;
        }
        return true;
    }

    private boolean isFibonacci(int n) {
        if (n < 2) return true;

        int fib1 = 0;
        int fib2 = 1;

        while (fib2 < n) {
            int fib3 = fib1 + fib2;
            fib1 = fib2;
            fib2 = fib3;
        }

        return fib2 == n;
    }
}

