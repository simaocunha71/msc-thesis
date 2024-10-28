You can parse the string using a loop and check each character. If the character is 'o', add 4 to the list. If the character is '|', add 2 to the list. If the character is '.', add 1 to the list. Here is the implementation in Java:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> parseMusic(String string) {
        List<Integer> beats = new ArrayList<>();
        for (int i = 0; i < string.length(); i++) {
            char c = string.charAt(i);
            if (c == 'o') {
                beats.add(4);
            } else if (c == '|') {
                beats.add(2);
            } else if (c == '.') {
                beats.add(1);
            }
        }
        return beats;
    }
}
```

This implementation has a time complexity of O(n), where n is the length of the input string.