        List<String> uniqueChars = new ArrayList<String>();
        String maxWord = "";
        int maxUnique = 0;

        for (String word : words) {
            uniqueChars.clear();
            for (char c : word.toCharArray()) {
                if (!uniqueChars.contains(String.valueOf(c))) {
                    uniqueChars.add(String.valueOf(c));
                }
            }

            if (uniqueChars.size() > maxUnique) {
                maxUnique = uniqueChars.size();
                maxWord = word;
            } else if (uniqueChars.size() == maxUnique) {
                if (word.compareTo(maxWord) < 0) {
                    maxWord = word;
                }
            }
        }

        return maxWord;
    }
}

// Time Complexity = O(n*m) where n is number of words and m is the average length of the words
// Space Complexity = O(m) because of the list uniqueChars that can potentially contain all the characters of the words.

```

This solution works by iterating through each word in the given list and then iterating through each character in the word. It checks if the character is already in the uniqueChars list. If it is not, it adds it to the list. The size of the uniqueChars list is then checked. If it is greater than maxUnique, the word and its size are updated. If the size is the same, the word is compared lexicographically and the one that comes first is updated. Finally, the word with the maximum number of unique characters is returned.


































































































































