        List<String> words = Arrays.asList(s.split(" "));
        List<String> result = new ArrayList<>();

        for (String word : words) {
            int count = 0;
            for (char c : word.toCharArray()) {
                if (isConsonant(c)) {
                    count++;
                }
            }
            if (count == n) {
                result.add(word);
            }
        }
        return result;
    }

    private boolean isConsonant(char c) {
        c = Character.toLowerCase(c);
        return c == 'b' || c == 'c' || c == 'd' || c == 'f' || c == 'g' || c == 'h'
                || c == 'j' || c == 'k' || c == 'l' || c == 'm' || c == 'n' || c == 'p'
                || c == 'q' || c == 'r' || c == 's' || c == 't' || c == 'v' || c == 'w'
                || c == 'x' || c == 'y' || c == 'z';
    }
}

The function `selectWords` splits the given string `s` into words using the `split` method. It then iterates over each word and counts the number of consonants. If the count equals `n`, it adds the word to the result list. The function returns the result list.

The helper function `isConsonant` checks whether a given character is a consonant by comparing it to a list of consonants. It converts the character to lowercase before checking, so it works for both uppercase and lowercase letters.

The complexity of this solution is O(n*m) where n is the number of words in the string and m is the length of the longest word. This is because for each word, we iterate through each character.

The space complexity is O(n) because we store the words in a list and the result list.

Test the function with different inputs to verify it works as expected.
*/

// 