```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean checkIfLastCharIsALetter(String txt) {
        if (txt == null || txt.length() == 0) {
            return false;
        }
        char lastChar = txt.charAt(txt.length() - 1);
        if (!Character.isLetter(lastChar)) {
            return false;
        }
        if (txt.charAt(txt.length() - 2) == ' ') {
            return true;
        }
        return false;
    }
}
```
