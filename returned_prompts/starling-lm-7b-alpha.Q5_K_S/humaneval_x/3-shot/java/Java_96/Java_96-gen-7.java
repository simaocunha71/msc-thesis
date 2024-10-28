        List<Integer> result = new ArrayList<>();
        if (n <= 1) return result;
        result.add(2);
        for (int i = 3; i < n; i++) {
            if (isPrime(i)) {
                result.add(i);
            }
        }
        return result;
    }

    private boolean isPrime(int n) {
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}

