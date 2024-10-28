```java
import java.util.*;
import java.lang.*;

class Solution {
    public int fizzBuzz(int n) {
        int count = 0;
        for (int i = 1; i < n; i++) {
            if (i % 11 == 0 || i % 13 == 0) {
                String numStr = Integer.toString(i);
                for (char c : numStr.toCharArray()) {
                    if (c == '7') {
                        count++;
                    }
                }
            }
        }
        return count;
    }
}
```
This solution iterates through all numbers less than n and checks if they are divisible by 11 or 13. If they are, it converts the number to a string and checks each character to see if it is '7'. If it is, it increments the count. Finally, it returns the count.