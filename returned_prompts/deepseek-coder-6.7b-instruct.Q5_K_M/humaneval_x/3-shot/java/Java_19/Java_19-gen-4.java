        Map<String, Integer> word_to_digit = new HashMap<>();
        word_to_digit.put("zero", 0);
        word_to_digit.put("one", 1);
        word_to_digit.put("two", 2);
        word_to_digit.put("three", 3);
        word_to_digit.put("four", 4);
        word_to_digit.put("five", 5);
        word_to_digit.put("six", 6);
        word_to_digit.put("seven", 7);
        word_to_digit.put("eight", 8);
        word_to_digit.put("nine", 9);

        List<String> number_words = Arrays.asList(numbers.split(" "));
        number_words.sort((a, b) -> word_to_digit.get(a) - word_to_digit.get(b));

        return String.join(" ", number_words);
     }
}

