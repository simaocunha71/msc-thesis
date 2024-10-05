    List<String> words = Arrays.asList(s.split(" "));
    List<String> result = new ArrayList<>();
    for (String word : words) {
        int count = 0;
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
                continue;
            } else {
                count++;
            }
        }
        if (count == n) {
            result.add(word);
        }
    }
    return result;
}

}

A: 
This code works by first splitting the input string s into a list of words. It then iterates over each word in the list. For each word, it iterates over each character in the word and checks if the character is a vowel. If it is, it skips to the next character. If it is not a vowel, it increments a counter. If the counter equals n, the word is added to the result list. The function then returns the result list.

