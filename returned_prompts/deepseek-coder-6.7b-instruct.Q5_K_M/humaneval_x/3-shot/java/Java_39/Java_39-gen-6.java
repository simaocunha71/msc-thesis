        List<Integer> fibPrimes = new ArrayList<Integer>();
        int a = 0;
        int b = 1;
        while (fibPrimes.size() < n) {
            int temp = a;
            a = b;
            b = temp + b;
            if (isPrime(b)) {
                fibPrimes.add(b);
            }
        }
        return fibPrimes.get(n - 1);
    }

    private boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}

