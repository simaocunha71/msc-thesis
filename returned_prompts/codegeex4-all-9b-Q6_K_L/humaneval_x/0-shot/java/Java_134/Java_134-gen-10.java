```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean checkIfLastCharIsALetter(String txt) {
        if (txt.length() == 0) return false;
        char lastChar = txt.charAt(txt.length() - 1);
        return Character.isLetter(lastChar) && !Character.isLetterOrDigit(txt.charAt(txt.length() - 2));
    }
}
```
