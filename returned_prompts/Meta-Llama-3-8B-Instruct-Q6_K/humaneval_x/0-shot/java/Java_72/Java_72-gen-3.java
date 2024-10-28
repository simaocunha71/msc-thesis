Here is a Java solution for the problem:
```java
import java.util.*;

class Solution {
    public boolean willItFly(List<Integer> q, int w) {
        // Check if the list is balanced (palindromic)
        List<Integer> reversedQ = new ArrayList<>(q);
        Collections.reverse(reversedQ);
        if (!reversedQ.equals(q)) {
            return false;
        }

        // Check if the sum of the list elements is less than or equal to the maximum possible weight
        int sum = 0;
        for (int num : q) {
            sum += num;
        }
        return sum <= w;
    }
}
```
This solution first checks if the list `q` is balanced by reversing the list and comparing it to the original list. If the lists are not equal, the function returns `false`, indicating that the object will not fly.

Then, the function calculates the sum of the list elements and checks if it is less than or equal to the maximum possible weight `w`. If the sum is less than or equal to `w`, the function returns `true`, indicating that the object will fly. Otherwise, it returns `false`.