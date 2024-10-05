```java
import java.util.*;
import java.lang.*;

class Solution {
    public int fruitDistribution(String s, int n) {
        String[] words = s.split(" ");
        int apples = 0, oranges = 0;
        for (String word : words) {
            if (word.contains("apples")) {
                apples = Integer.parseInt(word.split(" ")[0]);
            } else if (word.contains("oranges")) {
                oranges = Integer.parseInt(word.split(" ")[0]);
            }
        }
        return n - apples - oranges;
    }
}
```