        List<Integer> factors = new ArrayList<>();
        for (int i = 2; i <= n; i++) {
            if (n % i == 0) {
                factors.add(i);
            }
        }
        factors.sort(Collections.reverseOrder());

        for (int factor : factors) {
            if (isPrime(factor)) {
                return factor;
            }
        }
        return -1;
    }

    public boolean isPrime(int x) {
        if (x % 2 == 0) return false;

        for (int i = 3; i * i <= x; i += 2) {
            if (x % i == 0) return false;
        }
        return true;
    }
}

