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
        List<String> primeWords = new ArrayList<>();

        for (String word : sentence.split(" ")) {
            if (isPrime(word.length())) {
                primeWords.add(word);
            }
        }

        return String.join(" ", primeWords);
    }

    public boolean isPrime(int number) {
        if (number == 1 || number == 0) {
            return false;
        }

        for (int i = 2; i < number; i++) {
            if (number % i == 0) {
                return false;
            }
        }

        return true;
    }
}
