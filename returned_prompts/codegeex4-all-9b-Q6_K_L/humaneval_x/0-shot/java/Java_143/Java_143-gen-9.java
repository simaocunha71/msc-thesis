```java
import java.util.*;
import java.lang.*;

class Solution {
    public String wordsInSentence(String sentence) {
        if (sentence == null || sentence.length() == 0) {
            return "";
        }

        String[] words = sentence.split(" ");
        StringBuilder result = new StringBuilder();

        for (String word : words) {
            if (isPrime(word.length())) {
                result.append(word).append(" ");
            }
        }

        if (result.length() > 0) {
            result.deleteCharAt(result.length() - 1);
        }

        return result.toString();
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
}
```