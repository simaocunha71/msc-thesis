        List<Integer> result = new ArrayList<>();
        result.add(n);
        while (n != 1) {
            if (n % 2 == 0) {
                n = n / 2;
            } else {
                n = 3 * n + 1;
                result.add(n);
            }
        }
        return result.stream().filter(i -> i % 2 == 1).sorted().collect(Collectors.toList());
    }
}

