```java
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
        // Split the sentence into words
        String[] words = sentence.split(" ");

        // Initialize a StringBuilder to store the result
        StringBuilder result = new StringBuilder();

        // Iterate through each word
        for (String word : words) {
            // Check if the length of the word is a prime number
            if (isPrime(word.length())) {
                // If it is, append it to the result
                result.append(word).append(" ");
            }
        }

        // Remove the trailing space and return the result
        return result.toString().trim();
    }

    // Helper method to check if a number is prime
    private boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}
```
This solution splits the input sentence into words, checks if the length of each word is a prime number, and if so, appends it to the result string. The `isPrime` method checks if a number is prime by iterating from 2 to the square root of the number and checking if it is divisible by any number in that range. The trailing space is removed from the result string before it is returned.