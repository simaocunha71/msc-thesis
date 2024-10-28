Here is the Java code that solves the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int countUpper(String s) {
        int count = 0;
        for (int i = 0; i < s.length(); i += 2) {
            char c = s.charAt(i);
            if (c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U') {
                count++;
            }
        }
        return count;
    }
}
```

This code iterates over the string `s` at even indices and checks if the character is an uppercase vowel. If it is, it increments the `count` variable. Finally, it returns the `count` variable.