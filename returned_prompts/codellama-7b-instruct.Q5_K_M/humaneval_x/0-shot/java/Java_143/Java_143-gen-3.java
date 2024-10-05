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

        // Create a list of prime numbers
        List<Integer> primeList = new ArrayList<Integer>();
        for (int i = 2; i <= 100; i++) {
            if (isPrime(i)) {
                primeList.add(i);
            }
        }

        // Create a list of words from the sentence
        List<String> wordList = new ArrayList<String>();
        String[] words = sentence.split(" ");
        for (String word : words) {
            wordList.add(word);
        }

        // Return the words from the sentence whose lengths are prime numbers
        String primeWords = "";
        for (String word : wordList) {
            if (primeList.contains(word.length())) {
                primeWords += word + " ";
            }
        }

        return primeWords.trim();
    }

    // Check if a number is prime
    private boolean isPrime(int num) {
        if (num == 1 || num == 0) {
            return false;
        }
        for (int i = 2; i < num; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}
