```java
import java.util.*;
import java.lang.*;

class Solution {
    public int howManyTimes(String string, String substring) {
        return string.length() - string.replace(substring, "").length();
    }
}
```
This solution works by replacing all occurrences of the substring in the original string with an empty string, and then calculating the difference in length between the original string and the resulting string. The result is the number of times the substring appears in the original string.