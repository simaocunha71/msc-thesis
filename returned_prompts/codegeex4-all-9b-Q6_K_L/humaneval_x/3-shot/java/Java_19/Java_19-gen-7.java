        String[] numberals = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        Map<String, Integer> numberals_to_ints = new HashMap<>();

        for (int i = 0; i < numberals.length; i++) {
            numberals_to_ints.put(numberals[i], i);
        }

        String[] split_numbers = numbers.split(" ");
        Arrays.sort(split_numbers, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return numberals_to_ints.get(o1) - numberals_to_ints.get(o2);
            }
        });
        return String.join(" ", split_numbers);
    }
}

