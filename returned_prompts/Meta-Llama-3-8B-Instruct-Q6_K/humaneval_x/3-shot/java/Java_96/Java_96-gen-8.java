        List<Integer> result = new ArrayList<>();
        for (int i = 2; i < n; i++) {
            if (isPrime(i)) {
                result.add(i);
            }
        }
        return result;

    }

    private boolean isPrime(int number) {
        if (number < 2) return false;
        for (int i = 2, sqrt = (int) Math.sqrt(number); i <= sqrt; i++) {
            if (number % i == 0) return false;
        }
        return true;
    }
}

