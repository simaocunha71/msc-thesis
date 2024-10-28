```java
import java.util.*;

class Solution {
    public String wordsInSentence(String sentence) {
        String[] words = sentence.split(" ");
        StringBuilder result = new StringBuilder();
        for (String word : words) {
            if (isPrime(word.length())) {
                result.append(word).append(" ");
            }
        }
        return result.toString().trim();
    }

    private boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}
```
Explanation:
The problem requires us to filter the words from the given sentence whose lengths are prime numbers. We split the sentence into words and then iterate through each word. For each word, we check if its length is a prime number using the `isPrime` helper function. If the length is prime, we append the word to the result string. Finally, we trim the result string to remove any trailing spaces.

The `isPrime` function checks if a given number is prime. It does this by iterating from 2 to the square root of the number and checking if the number is divisible by any of these values. If it is, then the number is not prime and the function returns `false`. If the number is not divisible by any of these values, then it is prime and the function returns `true`.

The time complexity of this solution is O(n*m), where n is the number of words in the sentence and m is the maximum length of a word. This is because we are iterating through each word and checking its length. The space complexity is O(n), where n is the number of words in the sentence, as we are storing the filtered words in a string. 