```java
import java.util.*;
import java.lang.*;

class Solution {
    public String encrypt(String s) {
        return s.chars()
            .map(c -> (char)((c - 'a' + 4) % 26 + 'a'))
            .map(c -> (char)((c - 'A' + 4) % 26 + 'A'))
            .collect(StringBuilder::new, StringBuilder::appendCodePoint, StringBuilder::append)
            .toString();
    }
}
```