        List<Integer> digits = new ArrayList<>();
        while (x > 0) {
            digits.add(x % base);
            x /= base;
        }
        StringBuilder result = new StringBuilder();
        for (int i = digits.size() - 1; i >= 0; i--) {
            result.append(digits.get(i));
        }
        return result.toString();
    }
}

