The problem is asking to check if all numbers in the given list are below a certain threshold. We can achieve this by iterating through the list and checking if each number is less than the threshold. If any number is not less than the threshold, we can return false. If we have checked all numbers and none of them are not less than the threshold, we can return true.

Here is the solution in Java:

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

This solution has a time complexity of O(n), where n is the number of elements in the list, because we are iterating through the list once. The space complexity is O(1), because we are using a constant amount of space to store the threshold and the return value. 

You can test this function with the examples you provided:

```java
public static void main(String[] args) {
    List<Integer> list1 = Arrays.asList(1, 2, 4, 10);
    List<Integer> list2 = Arrays.asList(1, 20, 4, 10);
    System.out.println(new Solution().belowThreshold(list1, 100));  // true
    System.out.println(new Solution().belowThreshold(list2, 5));  // false
}
```  