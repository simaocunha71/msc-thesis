        List<String> words = Arrays.asList(s.split(" "));
        List<String> selectedWords = new ArrayList<>();

        for (String word : words) {
            if (countConsonants(word) == n) {
                selectedWords.add(word);
            }
        }

        return selectedWords;
    }

    private int countConsonants(String word) {
        int count = 0;
        for (char c : word.toCharArray()) {
            if (isConsonant(c)) {
                count++;
            }
        }
        return count;
    }

    private boolean isConsonant(char c) {
        c = Character.toLowerCase(c);
        return !(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u');
    }
}

The solution is simple. It splits the input string into words and iterates through the list of words. If the number of consonants in a word is equal to the provided integer `n`, then the word is added to the list of selected words.

The helper methods `countConsonants` and `isConsonant` are used to count the number of consonants in a word and to check if a character is a consonant respectively.

The time complexity of this solution is O(n), where n is the length of the input string. This is because each character in the string is visited once. The space complexity is also O(n) because of the space needed to store the list of words and the list of selected words.

This solution assumes that words are separated by spaces and that the string does not contain punctuation. If punctuation is included in the string, then it would need to be removed before the words are extracted. Similarly, if words are separated by other characters (such as commas or periods), then the string would need to be split on those characters as well.
