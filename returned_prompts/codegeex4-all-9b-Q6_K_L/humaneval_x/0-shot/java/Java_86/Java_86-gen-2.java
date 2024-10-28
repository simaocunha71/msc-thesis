Here is a Java solution:

```java
import java.util.*;

class Solution {
    public String antiShuffle(String s) {
        String[] words = s.split(" ");
        StringBuilder result = new StringBuilder();
        for (String word : words) {
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            result.append(new String(chars));
            result.append(" ");
        }
        return result.toString().trim();
    }
}
```

This solution works by splitting the input string into words, sorting each word's characters, and appending the sorted words to a StringBuilder with a space. The `trim()` method is used to remove the trailing space at the end of the result string.

Let's test the solution with the examples from the question:

```java
public static void main(String[] args) {
    Solution solution = new Solution();
    System.out.println(solution.antiShuffle("Hi")); // prints "Hi"
    System.out.println(solution.antiShuffle("hello")); // prints "ehllo"
    System.out.println(solution.antiShuffle("Hello World!!!")); // prints "Hello !!!Wdlor"
}
```

The output matches the expected results, so the solution is correct.