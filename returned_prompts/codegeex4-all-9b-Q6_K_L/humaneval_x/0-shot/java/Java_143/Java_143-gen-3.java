Here is a Java solution for the problem:

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
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }
}
```

The `wordsInSentence` function splits the sentence into words and checks if each word's length is a prime number using the `isPrime` helper function. If the length is prime, it appends the word to the result string. The final result is trimmed to remove any leading or trailing spaces.