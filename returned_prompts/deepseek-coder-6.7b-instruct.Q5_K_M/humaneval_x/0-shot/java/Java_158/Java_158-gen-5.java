        // Initializing an empty string to store the result
        String result = "";

        // Traverse through each word in the list
        for (String word : words) {

            // Creating a HashSet to store unique characters in the word
            Set<Character> uniqueChars = new HashSet<>();

            // Adding each character of the word to the HashSet
            for (char c : word.toCharArray()) {
                uniqueChars.add(c);
            }

            // Comparing the size of the HashSet with the size of the result
            // If the size of the HashSet is greater, assign the word to the result
            // If the size of the HashSet is equal, compare the words lexicographically and assign the lexicographically smaller word to the result
            if (uniqueChars.size() > result.length() || (uniqueChars.size() == result.length() && word.compareTo(result) < 0)) {
                result = word;
            }
        }

        // Return the result
        return result;
    }
}

The function works by iterating over each word in the input list, and for each word, it creates a HashSet to store the unique characters. It then compares the size of this HashSet to the size of the result string. If the size of the HashSet (i.e., the number of unique characters in the word) is greater, it assigns the word to the result. If the size of the HashSet is equal to the size of the result string, it compares the words lexicographically and assigns the lexicographically smaller word to the result. Finally, it returns the result.

The time complexity of this function is O(n*m), where n is the number of words and m is the length of the longest word. This is because for each word, it iterates over its characters, which takes O(m) time. The space complexity is O(n*m), because in the worst case, for each word, it may have to store all of its characters in the HashSet, which takes O(m) space.
