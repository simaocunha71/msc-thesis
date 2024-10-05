Here is a Java solution:

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
        System.out.println(solution.wordsInSentence("This is a test")); // "is"
        System.out.println(solution.wordsInSentence("lets go for swimming")); // "go for"
    }
}
```

This solution works by first splitting the sentence into words using the `split` method, then checking if the length of each word is a prime number using the `isPrime` method. If the length is a prime number, the word is added to a `StringBuilder`. Finally, the `StringBuilder` is converted to a string and any trailing spaces are removed using `trim`. The `isPrime` method checks if a number is a prime number by iterating from 2 to the square root of the number and checking if the number is divisible by any of these numbers.