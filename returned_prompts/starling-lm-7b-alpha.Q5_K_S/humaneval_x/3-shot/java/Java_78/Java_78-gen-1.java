        Set<Integer> prime_numbers = new HashSet<>();
        prime_numbers.add(2);
        prime_numbers.add(3);
        prime_numbers.add(5);
        prime_numbers.add(7);
        prime_numbers.add(11);
        prime_numbers.add(13);

        List<Integer> number_hex = new ArrayList<>();
        for (char c : num.toCharArray()) {
            if (c >= 48 && c <= 57) {
                number_hex.add(c - 48);
            } else if (c >= 65 && c <= 70) {
                number_hex.add(c - 55);
            } else if (c >= 71 && c <= 74) {
                number_hex.add(c - 67);
            } else if (c >= 85 && c <= 86) {
                number_hex.add(c - 83);
            } else if (c >= 87 && c <= 88) {
                number_hex.add(c - 85);
            } else if (c >= 97 && c <= 100) {
                number_hex.add(c - 95);
            } else if (c >= 101 && c <= 102) {
                number_hex.add(c - 103);
            } else if (c >= 117 && c <= 118) {
                number_hex.add(c - 115);
            }
        }

        int result = 0;
        for (int number : number_hex) {
            if (prime_numbers.contains(number)) result += 1;
        }

        return result;
    }
}

