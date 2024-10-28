```java
import java.util.*;
import java.lang.*;

class Solution {
    public Object splitWords(String txt) {
        if (!txt.contains(" ")) {
            if (!txt.contains(",")) {
                int count = 0;
                for (char c : txt.toCharArray()) {
                    if (Character.isLowerCase(c)) {
                        if ((int) c % 2 == 1) {
                            count++;
                        }
                    }
                }
                return count;
            } else {
                return Arrays.asList(txt.split(","));
            }
        } else {
            return Arrays.asList(txt.split(" "));
        }
    }
}
```