        List<Integer> result = new ArrayList<>();

        while (n != 0) {
            result.add(n);
            if (n % 2 == 0) {
                n = n / 2;
            } else {
                n = n + 1;
            }
        }
        return result;
    }
}

