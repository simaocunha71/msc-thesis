```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> sortArray(List<Integer> array) {
        int sum = array.get(0) + array.get(array.size() - 1);
        List<Integer> copy = new ArrayList<>(array);
        copy.sort(sum % 2 == 0 ? Comparator.reverseOrder() : Comparator.naturalOrder());
        return copy;
    }
}
```