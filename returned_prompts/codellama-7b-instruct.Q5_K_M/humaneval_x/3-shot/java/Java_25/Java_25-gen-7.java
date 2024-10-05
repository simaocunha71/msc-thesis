        List<Integer> result = new ArrayList<>();
        while (n % 2 == 0) {
            n /= 2;
            result.add(2);
        }

        for (int i = 3; i <= Math.sqrt(n); i += 2) {
            while (n % i == 0) {
                n /= i;
                result.add(i);
            }
        }
        if (n > 1) {
            result.add(n);
        }
        return result;
    }
}

