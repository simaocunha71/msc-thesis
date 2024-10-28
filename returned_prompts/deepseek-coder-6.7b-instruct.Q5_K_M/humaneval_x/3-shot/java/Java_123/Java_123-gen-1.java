        List<Integer> collatz = new ArrayList<>();
        while (n != 1) {
            if (n % 2 != 0) {
                collatz.add(n);
            }
            n = n % 2 == 0 ? n / 2 : 3 * n + 1;
        }
        collatz.add(1);
        collatz.sort(Integer::compareTo);
        return collatz;
    }
}

