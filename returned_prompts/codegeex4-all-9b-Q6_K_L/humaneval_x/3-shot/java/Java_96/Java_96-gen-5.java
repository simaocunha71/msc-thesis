        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            if (isPrime(i)) {
                result.add(i);
            }
        }
        return result;
    }

    private boolean isPrime(int n) {
        if (n <= 1) return false;
        for (int i = 2; i < n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}

