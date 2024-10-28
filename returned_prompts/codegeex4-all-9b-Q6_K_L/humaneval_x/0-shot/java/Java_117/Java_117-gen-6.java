```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> selectWords(String s, int n) {
        List<String> res = new ArrayList<>();
        if (s == null || s.isEmpty()) {
            return res;
        }
        String[] words = s.split(" ");
        for (String word : words) {
            int count = 0;
            for (char c : word.toCharArray()) {
                if (isConsonant(c)) {
                    count++;
                }
            }
            if (count == n) {
                res.add(word);
            }
        }
        return res;
    }

    private boolean isConsonant(char c) {
        c = Character.toLowerCase(c);
        return c >= 'b' && c <= 'z' && c != 'e' && c != 'i' && c != 'o' && c != 'u';
    }
}
```