```java
import java.util.*;
import java.lang.*;

class Solution {
    public int countUpper(String value) {
        int count = 0;
        for (char c : value.toCharArray()) {
            if (Character.isUpperCase(c)) {
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.countUpper("Hello World")); // Output: 2
    }
}
```
