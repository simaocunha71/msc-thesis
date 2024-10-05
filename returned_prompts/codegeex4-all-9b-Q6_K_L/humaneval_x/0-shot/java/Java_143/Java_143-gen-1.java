To solve this problem, we need to do the following steps:

1. Split the sentence into words using space as delimiter.
2. Check if the length of each word is a prime number.
3. If the length of a word is a prime number, add it to a new list.
4. Join the words in the new list into a string separated by a space.
5. Return the resulting string.

Here is the Java code that implements the above steps:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public String wordsInSentence(String sentence) {
        String[] words = sentence.split(" ");
        List<String> primeWords = new ArrayList<>();
        
        for (String word : words) {
            if (isPrime(word.length())) {
                primeWords.add(word);
            }
        }
        
        return String.join(" ", primeWords);
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

Let's test the code with the given examples:

```java
Solution solution = new Solution();
System.out.println(solution.wordsInSentence("This is a test")); // Output: "is"
System.out.println(solution.wordsInSentence("lets go for swimming")); // Output: "go for"
```

The code should output the expected results.