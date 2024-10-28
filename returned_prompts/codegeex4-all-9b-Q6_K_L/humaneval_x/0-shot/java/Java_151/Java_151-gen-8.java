Here is a solution in Java:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int doubleTheDifference(List<Object> lst) {
        int sum = 0;
        for (Object obj : lst) {
            if (obj instanceof Integer) {
                int num = (Integer) obj;
                if (num > 0 && num % 2 != 0) {
                    sum += num * num;
                }
            }
        }
        return sum;
    }
}
```
In this solution, we iterate through each item in the list. We check if the item is an instance of `Integer` to avoid ClassCastException. If it is an instance of `Integer`, we check if it is a positive odd number. If it is, we add its square to the sum. Finally, we return the sum. If the list is empty, the sum will be 0, so the function will return 0 in that case as well.