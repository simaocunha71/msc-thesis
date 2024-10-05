```java
import java.util.*;
import java.lang.*;

class Solution {
    public Object splitWords(String txt) {
        if(txt.contains(" ")) {
            return txt.split(" ");
        } else if(txt.contains(",")) {
            return txt.split(",");
        } else {
            int count = 0;
            for(int i = 0; i < txt.length(); i++) {
                char c = txt.charAt(i);
                if(Character.isLowerCase(c) && (c - 'a') % 2 == 1) {
                    count++;
                }
            }
            return count;
        }
    }
}
```