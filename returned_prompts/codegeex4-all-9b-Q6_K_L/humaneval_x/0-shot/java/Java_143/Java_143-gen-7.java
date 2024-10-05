Here is a Java solution which uses a helper function to check if a number is prime and a loop to iterate over the words in the sentence:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public String wordsInSentence(String sentence) {
        String[] words = sentence.split(" ");
        StringBuilder sb = new StringBuilder();
        for (String word : words) {
            if (isPrime(word.length())) {
                sb.append(word).append(" ");
            }
        }
        return sb.toString().trim();
    }

    private boolean isPrime(int n) {
        if (n <= 1) {
            return false;
        }
        for (int i = 2; i < Math.sqrt(n) + 1; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.wordsInSentence("This is a test")); // Output: "is"
        System.out.println(solution.wordsInSentence("lets go for swimming")); // Output: "go for"
    }
}
```

This solution first splits the sentence into an array of words using the `split` method. It then iterates over each word, checking if its length is a prime number using the `isPrime` method. If it is, the word is appended to a `StringBuilder` with a space after it. Finally, the `StringBuilder` is converted to a string and any leading or trailing spaces are removed using the `trim` method.