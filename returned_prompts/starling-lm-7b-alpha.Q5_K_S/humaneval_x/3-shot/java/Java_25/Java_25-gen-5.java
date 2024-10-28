        List<Integer> result = new ArrayList<>();

        for (int d = 2; d * d <= n; d++) {
            while (n % d == 0) {
                result.add(d);
                n /= d;
            }
        }
        if (n != 1) result.add(n);
        return result;
    }
}

