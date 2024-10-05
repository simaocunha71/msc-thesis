        List<Integer> digits = new ArrayList<>();
        int current = x;
        while (current > 0) {
            digits.add(current % 10);
            current /= 10;
        }

        Collections.reverse(digits);
        for (int i = 0; i < shift; i++) {
            digits.add(digits.get(i));
        }
        Collections.reverse(digits);

        StringBuilder result = new StringBuilder();
        for (int d : digits) {
            result.append(d);
        }
        return result.toString();
    }
}

