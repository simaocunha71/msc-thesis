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

    private boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}
```

Explanation:
The solution iterates over the words in the sentence and checks if the length of each word is a prime number using the `isPrime` function. If the length is prime, the word is added to the result. Finally, the result is trimmed to remove any trailing spaces.

The `isPrime` function checks if a number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of these values. If it is, the function returns false, indicating that the number is not prime. If the function reaches the end of the loop without finding a divisor, it returns true, indicating that the number is prime.

This solution has a time complexity of O(n*m) where n is the number of words in the sentence and m is the average length of the words, and a space complexity of O(n) for the result.