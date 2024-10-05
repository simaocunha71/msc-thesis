```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> sortArray(List<Integer> array) {
        if(array == null || array.size() == 0) {
            return array;
        }
        int sum = array.get(0) + array.get(array.size() - 1);
        List<Integer> sortedArray = new ArrayList<>(array);
        if(sum % 2 == 0) {
            Collections.sort(sortedArray, Collections.reverseOrder());
        } else {
            Collections.sort(sortedArray);
        }
        return sortedArray;
    }
}
```