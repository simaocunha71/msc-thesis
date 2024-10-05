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

    public boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}
```

The code defines a class `Solution` with a method `wordsInSentence` that takes a string `sentence` as input and returns a new string containing only the words from the original sentence whose lengths are prime numbers. The method uses a `StringBuilder` object to build the result string and a helper method `isPrime` to check if a number is prime.

The `isPrime` method checks if a number `n` is prime by iterating from 2 to the square root of `n` and checking if `n` is divisible by any of these numbers. If `n` is divisible, it is not a prime number, so the method returns `false`. Otherwise, it returns `true`.

In the `wordsInSentence` method, the code splits the input sentence into individual words using the `split` method, then iterates over the words and checks if the length of each word is prime using the `isPrime` method. If the length is prime, the word is appended to the result string. Finally, the method returns the result string after trimming any trailing spaces.

The code can be tested with the provided examples:
```java
public static void main(String[] args) {
    Solution solution = new Solution();
    System.out.println(solution.wordsInSentence("This is a test")); // Output: "is"
    System.out.println(solution.wordsInSentence("lets go for swimming")); // Output: "go for"
}
```  |  See more at: https://www.educative.io/eduhub/words-in-sentence#L1R1P1  |  Variations: |  #Java #String #PrimeNumbers  |  #Algorithm  |  #StringManipulation  |  #PrimeCheck  |  #StringBuilder  |  #StringSplit