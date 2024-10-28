Here is the solution:
```java
import java.util.*;

class Solution {
    public boolean willItFly(List<Integer> q, int w) {
        // Check if the list is balanced (palindromic)
        int leftSum = 0;
        for (int i = 0; i < q.size() / 2; i++) {
            leftSum += q.get(i);
        }
        int rightSum = 0;
        for (int i = q.size() - 1; i >= q.size() / 2; i--) {
            rightSum += q.get(i);
        }
        return leftSum == rightSum && leftSum <= w;
    }
}
```
This solution works by first calculating the sum of the elements on the left side of the list and the sum of the elements on the right side. If the two sums are equal, then the list is balanced. It then checks if the sum of the elements is less than or equal to the maximum possible weight w. If both conditions are met, the function returns true, indicating that the object will fly. Otherwise, it returns false.