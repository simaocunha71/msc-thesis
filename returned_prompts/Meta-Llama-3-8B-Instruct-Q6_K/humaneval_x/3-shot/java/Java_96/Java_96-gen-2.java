        List<Integer> result = new ArrayList<>();
        for (int i = 2; i < n; i++) {
            if (isPrime(i)) {
                result.add(i);
            }
        }
        return result;
    }

    public boolean isPrime(int number) {
        if (number <= 1) {
            return false;
        }
        for (int i = 2; i * i <= number; i++) {
            if (number % i == 0) {
                return false;
            }
        }
        return true;
    }
}

