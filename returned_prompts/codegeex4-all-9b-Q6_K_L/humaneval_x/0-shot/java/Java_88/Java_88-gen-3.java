```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> sortArray(List<Integer> array) {
        if (array.size() <= 1) {
            return array;
        }

        int sum = array.get(0) + array.get(array.size() - 1);
        Collections.sort(array);

        if (sum % 2 == 0) {
            Collections.reverse(array);
        }

        return array;
    }
}
```