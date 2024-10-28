        List<Integer> result = new ArrayList<>();
        while (n != 1) {
            if (n % 2 == 0) {
                n = n / 2;
            } else {
                n = n * 3 + 1;
            }
            if (n % 2 != 0) {
                result.add(n);
            }
        }
        result.add(1);
        Collections.sort(result);
        return result;
    }
}

