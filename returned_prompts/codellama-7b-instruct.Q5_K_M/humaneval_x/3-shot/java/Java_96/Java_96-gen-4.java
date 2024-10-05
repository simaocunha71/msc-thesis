        List<Integer> result = new ArrayList<>();

        if (n <= 0) return result;

        for (int i = 2; i < n; i++) {
            if (isPrime(i)) result.add(i);
        }
        return result;
    }

    public boolean isPrime(int i) {
        if (i <= 1) return false;

        for (int j = 2; j < i; j++) {
            if (i % j == 0) return false;
        }
        return true;
    }
}

