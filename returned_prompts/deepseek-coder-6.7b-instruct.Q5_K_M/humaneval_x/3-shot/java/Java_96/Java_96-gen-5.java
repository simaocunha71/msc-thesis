        List<Integer> primes = new ArrayList<>();
        for  (int i = 2; i < n; i++) {
            if  (isPrime(i)) {
                primes.add(i);
            }
        }
        return primes;
    }

    private boolean isPrime(int num) {
        if  (num <= 1) {
            return false;
        }
        for  (int i = 2; i * i <= num; i++) {
            if  (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}

