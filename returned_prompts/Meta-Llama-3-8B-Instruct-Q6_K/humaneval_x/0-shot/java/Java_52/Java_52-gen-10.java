Here is a simple solution in Java that checks if all numbers in the list are below the threshold:

```java
import java.util.*;

class Solution {
    public boolean belowThreshold(List<Integer> l, int t) {
        for (int num : l) {
            if (num >= t) {
                return false;
            }
        }
        return true;
    }
}
```

This solution iterates over each number in the list. If it finds a number that is greater than or equal to the threshold, it immediately returns `false`. If it iterates over the entire list without finding such a number, it returns `true`. 

You can use this solution like this:

```java
public static void main(String[] args) {
    List<Integer> list1 = Arrays.asList(1, 2, 4, 10);
    List<Integer> list2 = Arrays.asList(1, 20, 4, 10);
    Solution solution = new Solution();
    System.out.println(solution.belowThreshold(list1, 100));  // prints: true
    System.out.println(solution.belowThreshold(list2, 5));    // prints: false
}
```

In this example, the first list contains numbers less than 100, so the method returns `true`. The second list contains numbers greater than 5, so the method returns `false`. 