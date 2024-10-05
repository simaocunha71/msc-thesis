You can iterate over the list and check if the index is even and the number is odd, then add it to the sum. Here's the code:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int solution(List<Integer> lst) {
        int sum = 0;
        for (int i = 0; i < lst.size(); i += 2) {
            if (lst.get(i) % 2 != 0) {
                sum += lst.get(i);
            }
        }
        return sum;
    }
}
```