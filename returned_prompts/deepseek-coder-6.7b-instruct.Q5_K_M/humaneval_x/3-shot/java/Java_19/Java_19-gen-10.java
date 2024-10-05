        Map<String, Integer> numbers_to_strings = new HashMap<>();
        numbers_to_strings.put("zero", 0);
        numbers_to_strings.put("one", 1);
        numbers_to_strings.put("two", 2);
        numbers_to_strings.put("three", 3);
        numbers_to_strings.put("four", 4);
        numbers_to_strings.put("five", 5);
        numbers_to_strings.put("six", 6);
        numbers_to_strings.put("seven", 7);
        numbers_to_strings.put("eight", 8);
        numbers_to_strings.put("nine", 9);

        String[] number_strings = numbers.split(" ");
        Integer[] number_values = new Integer[number_strings.length];

        for  (int i = 0; i < number_strings.length; i++) {
            number_values[i] = numbers_to_strings.get(number_strings[i]);
        }

        Arrays.sort(number_values);

        for  (int i = 0; i < number_strings.length; i++) {
            number_strings[i] = "";
            for  (Map.Entry<String, Integer> entry : numbers_to_strings.entrySet()) {
                if  (entry.getValue() == number_values[i]) {
                    number_strings[i] = entry.getKey();
                    break;
                }
            }
        }

        return String.join(" ", number_strings);
    }
}

