```java
import java.util.*;
import java.lang.*;

class Solution {
    public int hexKey(String num) {
        int count = 0;
        for (char c : num.toCharArray()) {
            switch (c) {
                case '2':
                case '3':
                case '5':
                case '7':
                case 'B':
                case 'D':
                    count++;
                    break;
            }
        }
        return count;
    }
}
```