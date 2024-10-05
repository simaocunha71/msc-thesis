        List<Integer> result = new ArrayList<>();
        while (n % 2 == 0) {
            result.add(2);
            n /= 2;
        }

        for (int i = 3; i * i <= n; i += 2) {
            while (n % i == 0) {
                result.add(i);
                n /= i;
            }
        }

        if (n > 2) result.add(n);
        return result;
    }
}

