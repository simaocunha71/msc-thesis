        List<Integer> digits = new ArrayList<>();
        for (int i = x; i > 0; i /= 10) {
            digits.add(i % 10);
        }
        for (int i = 0; i < shift % digits.size(); i++) {
            digits.add(digits.get(0));
            digits.remove(0);
        }
        return digits.stream().map(String::valueOf).collect(Collectors.joining());
    }
}

