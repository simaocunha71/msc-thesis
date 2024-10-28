        List<Integer> result = new ArrayList<>();
        result.add(n);

        while (n != 1) {
            if ((n % 2) == 0) {
                n = n / 2;
            } else {
                n = n * 3 + 1;
            }
            if (!result.contains(n)) {
                result.add(n);
            }
        }
        result.sort(Comparator.naturalOrder());
        return result.subList(1, result.size());
    }
}

