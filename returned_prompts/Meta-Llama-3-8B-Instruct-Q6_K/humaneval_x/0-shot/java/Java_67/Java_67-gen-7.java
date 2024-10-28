Here is a simple solution in Java:

```java
import java.util.*;

class Solution {
    public int fruitDistribution(String s, int n) {
        int apples = 0, oranges = 0;
        String[] words = s.split(" ");
        for (String word : words) {
            if (word.equals("apples")) {
                apples = Integer.parseInt(words[words.length - 1]);
            } else if (word.equals("oranges")) {
                oranges = Integer.parseInt(words[words.length - 2]);
            }
        }
        return n - apples - oranges;
    }
}
```
This solution works by splitting the input string into words and then finding the number of apples and oranges. It does this by checking each word to see if it is "apples" or "oranges" and then parsing the following word as an integer. Finally, it returns the total number of fruits minus the number of apples and oranges. This solution assumes that the input string is always in the correct format. If the input string can be in a different format, you would need to add error checking code. 