        List<Integer> result = new ArrayList<>();
        int i = 2;

        while (i * i <= n) {
            while (n % i == 0) {
                result.add(i);
                n /= i;
            }
            i += 1;
        }

        if (n > 1) {
            result.add(n);
        }
        return result;
    }
}