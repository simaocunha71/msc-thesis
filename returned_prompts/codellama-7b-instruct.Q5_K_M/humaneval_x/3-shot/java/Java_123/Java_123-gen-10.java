        List<Integer> result = new ArrayList<>();

        while (n > 1) {
            if (n % 2 == 0) {
                n /= 2;
            } else {
                n = 3 * n + 1;
            }
            result.add(n);
        }
        return result;
    }
}

