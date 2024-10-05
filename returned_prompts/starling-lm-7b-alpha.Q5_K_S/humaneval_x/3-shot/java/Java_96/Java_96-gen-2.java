        List<Integer> result = new ArrayList<>();
        if (n <= 1) return result;
        result.add(2);
        if (n <= 2) return result;
        result.add(3);
        if (n <= 3) return result;
        for (int i = 5; i <= n; i += 2) {
            if (isPrime(i)) result.add(i);
        }
        return result;
    }

    private boolean isPrime(int number) {
        if (number <= 3) return true;
        if (number % 2 == 0) return false;
        if (number % 3 == 0) return false;
        int i = 5;
        while (i * i <= number) {
            if (number % i == 0) return false;
            if (number % (i + 2) == 0) return false;
            i += 6;
        }
        return true;
    }
}

