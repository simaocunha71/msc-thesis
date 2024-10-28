        List<Integer> result = new ArrayList<>();
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                result.add(i);
                while (n % i == 0) {
                    n = n / i;
                }
            }
        }
        if (n != 1) result.add(n);
        return result;
    }
}

