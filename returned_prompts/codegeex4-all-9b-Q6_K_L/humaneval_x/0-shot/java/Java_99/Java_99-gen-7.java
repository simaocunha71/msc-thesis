Here is the solution using Java:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int countUpper(String value) {
        int n = 0;
        for (int i = 0; i < value.length(); i++) {
            if (value.charAt(i) >= '0' && value.charAt(i) <= '9') {
                n++;
            }
        }
        return n;
    }
}
```

This function takes a string as an input and counts the number of digits in it. It does this by iterating over each character in the string and checking if it is a digit. If it is, it increments the count. Finally, it returns the count.

For example, if you call `countUpper("10")`, it will return 2 because there are two digits in the string. If you call `countUpper("15.3")`, it will return 2 because there are two digits in the string.