Here is a solution in Java:

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
        if (sb.length() > 0) {
            sb.deleteCharAt(sb.length() - 1);
        }
        return sb.toString();
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
        System.out.println(solution.wordsInSentence("This is a test"));
        System.out.println(solution.wordsInSentence("lets go for swimming"));
    }
}
```

The main idea of the solution is to split the input sentence into words, then check if the length of each word is a prime number. If it is, append it to the result string. Finally, return the result string. The `isPrime` method checks if a number is a prime number or not.