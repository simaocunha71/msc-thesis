import java.util.*;
import java.lang.*;

class Solution {
    /**
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
     */
    public String wordsInSentence(String sentence) {
        List<String> words = new ArrayList<>();
        String[] sentenceArray = sentence.split(" ");
        for (int i = 0; i < sentenceArray.length; i++) {
            if (isPrime(sentenceArray[i].length())) {
                words.add(sentenceArray[i]);
            }
        }
        StringBuilder newSentence = new StringBuilder();
        for (String word : words) {
            newSentence.append(word).append(" ");
        }
        return newSentence.toString().trim();
    }
    private boolean isPrime(int n) {
        if (n == 1 || n == 0) return false;
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}
