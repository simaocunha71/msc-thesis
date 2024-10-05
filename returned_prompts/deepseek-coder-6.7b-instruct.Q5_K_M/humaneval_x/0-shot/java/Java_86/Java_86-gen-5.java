        // Convert the sentence to an array of words
        String[] words = s.split(" ");

        // Create a list to store the sorted words
        List<String> sortedWords = new ArrayList<>();

        // Sort each word and add it to the list
        for (String word : words) {
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            sortedWords.add(new String(chars));
        }

        // Join the sorted words back into a sentence
        String sortedSentence = String.join(" ", sortedWords);

        // Return the sorted sentence
        return sortedSentence;
    }
}

In this solution, the function `antiShuffle` takes a string `s` as input, splits it into words using the `split` method, and for each word, it converts it to a character array, sorts it using `Arrays.sort`, and then adds the sorted word to a list of sorted words. Finally, it joins the sorted words back together into a sentence using `String.join` and returns this sorted sentence.

This solution has a time complexity of O(n log n), where n is the length of the string. This is because for each word in the string, we are sorting the characters of the word, which takes O(log n) time. We are doing this for each word in the string, so the total time complexity is O(n log n).

The space complexity is O(n), where n is the length of the string. This is because we are storing the words in the string in a list, and the list can contain up to n words.

Note: The function `antiShuffle` only sorts the characters in each word and keeps the order of words and blank spaces in the sentence. The order of characters in each word is not changed, only the order of the words in the sentence is changed.

This solution assumes that the input string is a sentence where words are separated by spaces and punctuation is not considered as part of a word. If you want to handle punctuation as part of a word, you would need to modify the solution to handle this case.

Also, this solution does not handle uppercase letters. If you want to handle uppercase letters, you would need to add a step to