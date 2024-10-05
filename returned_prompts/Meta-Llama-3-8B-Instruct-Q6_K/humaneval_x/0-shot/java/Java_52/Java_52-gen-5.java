Here is a simple solution in Java:

```java
import java.util.*;

class Solution {
    public boolean belowThreshold(List<Integer> l, int t) {
        for (int i : l) {
            if (i >= t) {
                return false;
            }
        }
        return true;
    }
}
```

This function iterates over each number in the list. If it finds a number that is greater than or equal to the threshold, it immediately returns `false`. If it iterates over the entire list without finding such a number, it returns `true`. 

You can test this function with the examples you provided:

```java
public static void main(String[] args) {
    Solution solution = new Solution();
    System.out.println(solution.belowThreshold(Arrays.asList(1, 2, 4, 10), 100));  // prints: true
    System.out.println(solution.belowThreshold(Arrays.asList(1, 20, 4, 10), 5));  // prints: false
}
```

This will output:

```
true
false
``` 