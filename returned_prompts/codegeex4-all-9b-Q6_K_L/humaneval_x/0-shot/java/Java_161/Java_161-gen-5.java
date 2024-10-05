```java
import java.util.*;
import java.lang.*;

class Solution {
    public String solve(String s) {
        List<Character> letters = new ArrayList<>();
        for (char c : s.toCharArray()) {
            if (Character.isLetter(c)) {
                letters.add(c);
            }
        }
        StringBuilder result = new StringBuilder();
        if (letters.isEmpty()) {
            for (int i = s.length() - 1; i >= 0; i--) {
                result.append(s.charAt(i));
            }
        } else {
            int letterIndex = 0;
            for (int i = 0; i < s.length(); i++) {
                if (Character.isLetter(s.charAt(i))) {
                    result.append(Character.isLowerCase(letters.get(letterIndex)) ? Character.toUpperCase(letters.get(letterIndex)) : Character.toLowerCase(letters.get(letterIndex)));
                    letterIndex++;
                } else {
                    result.append(s.charAt(i));
                }
            }
        }
        return result.toString();
    }
}
```