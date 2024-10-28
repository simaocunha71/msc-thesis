```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> selectWords(String s, int n) {
        List<String> result = new ArrayList<>();
        String[] words = s.split(" ");
        for (String word : words) {
            int count = 0;
            for (char c : word.toCharArray()) {
                if (!"aeiouAEIOU".contains(String.valueOf(c))) {
                    count++;
                }
            }
            if (count == n) {
                result.add(word);
            }
        }
        return result;
    }
}
```