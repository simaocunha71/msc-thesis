        String maxWord = "";
        int maxCount = 0;

        for (String word : words) {
            Set<Character> uniqueChars = new HashSet<>();
            for (char c : word.toCharArray()) {
                uniqueChars.add(c);
            }
            if (uniqueChars.size() > maxCount) {
                maxCount = uniqueChars.size();
                maxWord = word;
            } else if (uniqueChars.size() == maxCount) {
                maxWord = maxWord.compareTo(word) < 0 ? maxWord : word;
            }
        }

        return maxWord;
    }
}

This program works by iterating over each word in the list of words and for each word, it counts the number of unique characters. If the count of unique characters of a word is greater than the current maxCount, it updates maxCount and maxWord with the current word. If the count of unique characters is equal to the current maxCount, it compares the current word and maxWord lexicographically and updates maxWord if the current word comes lexicographically first. Finally, it returns the word with the maximum number of unique characters.















































































