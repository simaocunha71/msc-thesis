        Set<Integer> all_numbers = new HashSet<>();
        Set<Integer> duplicates = new HashSet<>();

        for (int number : numbers) {
            if (all_numbers.contains(number)) {
                duplicates.add(number);
            } else {
                all_numbers.add(number);
            }
        }

        return new ArrayList<>(duplicates);
    }
}

