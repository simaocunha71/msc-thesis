        List<Integer> result = new ArrayList<>();
        while (n != 1) {
            if (n % 2 == 1) {
                result.add(n);
                n = 3 * n + 1;
            } else {
                n /= 2;
            }
        }
        return result;
    }
}

