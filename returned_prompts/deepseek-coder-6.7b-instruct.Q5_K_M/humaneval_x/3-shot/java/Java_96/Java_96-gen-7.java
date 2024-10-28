        List<Integer> primes = new ArrayList<>();
        for  (int i = 2; i < n; i++) {
            if  (isPrime(i)) {
                primes.add(i);
            }
        }
        return primes;
    }

    private boolean isPrime(int number) {
        if  (number <= 1) {
            return false;
        }
        for  (int i = 2; i < number; i++) {
            if  (number % i == 0) {
                return false;
            }
        }
        return true;
    }
}

