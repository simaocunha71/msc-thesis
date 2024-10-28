```java
import java.util.*;
import java.lang.*;

class Solution {
    public int digitSum(String s) {
        int sum = 0;
        for(int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if(Character.isUpperCase(c)) {
                sum += (int) c;
            }
        }
        return sum;
    }
}
```