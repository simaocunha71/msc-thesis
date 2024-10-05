        List<Integer> factors = new ArrayList<>();
        int i = 2;
        while (i * i <= n) {
            if (n % i == 0) {
                factors.add(i);
            }
            i += 1;
        }
        factors.add(n);
        int result = 1;
        for (int factor : factors) {
            result = Math.max(result, factor);
        }
        return result;
    }
}

