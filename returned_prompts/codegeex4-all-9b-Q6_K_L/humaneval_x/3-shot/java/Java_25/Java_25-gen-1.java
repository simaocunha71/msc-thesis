        List<Integer> factors = new ArrayList<>();
        int divisor = 2;

        while (n > 1) {
            if (n % divisor == 0) {
                factors.add(divisor);
                n /= divisor;
            } else {
                divisor += 1;
            }
        }
        return factors;
    }
}

