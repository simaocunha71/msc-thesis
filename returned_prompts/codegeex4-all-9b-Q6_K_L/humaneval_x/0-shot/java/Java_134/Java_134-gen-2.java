```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean checkIfLastCharIsALetter(String txt) {
        if (txt.isEmpty()) return false;
        char lastChar = txt.charAt(txt.length() - 1);
        return Character.isAlphabetic(lastChar) && !Character.isLetter(txt.charAt(txt.length() - 2));
    }
}
```
