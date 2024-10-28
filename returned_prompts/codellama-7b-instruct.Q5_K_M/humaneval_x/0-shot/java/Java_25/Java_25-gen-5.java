        List<Integer> primeFactors = new ArrayList<Integer>();
        for (int i = 2; i <= n; i++) {
            while (n % i == 0) {
                primeFactors.add(i);
                n /= i;
            }
            if (n == 1) {
                break A;
            }
        }
        return primeFactors;
    }
}
