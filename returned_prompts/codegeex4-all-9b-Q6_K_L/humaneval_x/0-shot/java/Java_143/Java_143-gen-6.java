To solve this problem, you can first split the sentence into words using the `split()` method. Then, you can iterate through the words and check if the length of each word is a prime number. If it is, you can add it to a result string. Finally, you can return the result string.

Here's the implementation in Java:

```java
import java.util.*;
import java.lang.*;

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
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        String sentence1 = "This is a test";
        System.out.println(solution.wordsInSentence(sentence1));  // Output: "is"

        String sentence2 = "lets go for swimming";
        System.out.println(solution.wordsInSentence(sentence2));  // Output: "go for"
    }
}
```

In the `isPrime()` method, we check if the number is less than or equal to 1, and if so, return `false`. Then, we iterate from 2 to the square root of the number and check if the number is divisible by any of these values. If it is, we return `false`. If none of these conditions are met, we return `true`, indicating that the number is prime.