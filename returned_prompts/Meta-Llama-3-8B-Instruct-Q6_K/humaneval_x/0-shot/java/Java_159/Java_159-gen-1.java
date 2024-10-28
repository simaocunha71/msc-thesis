Here is a Java solution for the problem:

```java
import java.util.*;

class Solution {
    public List<Integer> eat(int number, int need, int remaining) {
        int total = number + need;
        if (total > remaining) {
            total = remaining;
        }
        int left = remaining - total;
        return Arrays.asList(total, left);
    }
}
```
This solution calculates the total number of carrots eaten by adding the number of carrots already eaten and the number of carrots needed. Then, it checks if the total number of carrots eaten exceeds the remaining number of carrots. If it does, it sets the total number of carrots eaten to the remaining number of carrots. Finally, it returns a list containing the total number of carrots eaten and the number of carrots left.