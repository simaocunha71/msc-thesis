```java
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> howManyTimes("", "a")
    0
    >>> howManyTimes("aaa", "a")
    3
    >>> howManyTimes("aaaa", "aa")
    3
     */
    public int howManyTimes(String string, String substring) {
        if(substring.isEmpty()) return 0;
        int count = 0;
        int idx = string.indexOf(substring);
        while(idx != -1){
            count++;
            idx = string.indexOf(substring, idx + 1);
        }
        return count;
    }
}
```
