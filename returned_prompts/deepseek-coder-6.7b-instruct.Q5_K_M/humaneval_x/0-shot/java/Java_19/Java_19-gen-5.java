        String[] numberWords = numbers.split(" ");
        String[] numberList = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        HashMap<String, Integer> wordToNumber = new HashMap<>();
        for (int i = 0; i < numberList.length; i++) {
            wordToNumber.put(numberList[i], i);
        }
        Arrays.sort(numberWords, new Comparator<String>() {
            public int compare(String s1, String s2) {
                return wordToNumber.get(s1) - wordToNumber.get(s2);
            }
        });
        return String.join(" ", numberWords);
    }
}

