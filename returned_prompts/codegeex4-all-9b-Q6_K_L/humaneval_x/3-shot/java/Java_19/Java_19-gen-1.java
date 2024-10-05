        Map<String, Integer> number_to_int = new HashMap<>();
        number_to_int.put("zero", 0);
        number_to_int.put("one", 1);
        number_to_int.put("two", 2);
        number_to_int.put("three", 3);
        number_to_int.put("four", 4);
        number_to_int.put("five", 5);
        number_to_int.put("six", 6);
        number_to_int.put("seven", 7);
        number_to_int.put("eight", 8);
        number_to_int.put("nine", 9);

        String[] numberals = numbers.split(" ");
        Integer[] ints = new Integer[numberals.length];

        for (int i = 0; i < numberals.length; i++) {
            ints[i] = number_to_int.get(numberals[i]);
        }

        Arrays.sort(ints);

        StringBuilder result = new StringBuilder();
        for (int i : ints) {
            result.append(number_to_int.get(i));
            result.append(' ');
        }
        result.setLength(result.length() - 1);
        return result.toString();
    }
}

