        Map<String, Integer> wordToNumber = new HashMap<>();
        wordToNumber.put("zero", 0);
        wordToNumber.put("one", 1);
        wordToNumber.put("two", 2);
        wordToNumber.put("three", 3);
        wordToNumber.put("four", 4);
        wordToNumber.put("five", 5);
        wordToNumber.put("six", 6);
        wordToNumber.put("seven", 7);
        wordToNumber.put("eight", 8);
        wordToNumber.put("nine", 9);

        Map<Integer, String> numberToWord = new HashMap<>();
        numberToWord.put(0, "zero");
        numberToWord.put(1, "one");
        numberToWord.put(2, "two");
        numberToWord.put(3, "three");
        numberToWord.put(4, "four");
        numberToWord.put(5, "five");
        numberToWord.put(6, "six");
        numberToWord.put(7, "seven");
        numberToWord.put(8, "eight");
        numberToWord.put(9, "nine");

        List<Integer> sortedNumbers = new ArrayList<>();
        for  (String word : numbers.split(" ")) {
            sortedNumbers.add(wordToNumber.get(word));
        }

        Collections.sort(sortedNumbers);

        StringBuilder result = new StringBuilder();
        for  (Integer number : sortedNumbers) {
            result.append(numberToWord.get(number)).append(" ");
        }

        return result.toString().trim();
     }
}

