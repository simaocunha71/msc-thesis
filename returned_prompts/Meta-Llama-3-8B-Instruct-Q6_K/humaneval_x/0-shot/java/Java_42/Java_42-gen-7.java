The problem is asking you to create a method that takes a list of integers as an input and returns a new list where each element in the original list is incremented by 1.

Here is the solution in Java:

```java
import java.util.*;

class Solution {
    public List<Integer> incrList(List<Integer> l) {
        List<Integer> result = new ArrayList<>();
        for (int i : l) {
            result.add(i + 1);
        }
        return result;
    }
}
```

You can test this method with the following code:

```java
public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        List<Integer> l = Arrays.asList(1, 2, 3);
        List<Integer> result = solution.incrList(l);
        System.out.println(result); // prints [2, 3, 4]

        l = Arrays.asList(5, 3, 5, 2, 3, 3, 9, 0, 123);
        result = solution.incrList(l);
        System.out.println(result); // prints [6, 4, 6, 3, 4, 4, 10, 1, 124]
    }
}
```

This solution uses a for-each loop to iterate over the input list, adds each element incremented by 1 to a new list, and then returns the new list. The test cases in the main method demonstrate the functionality of the method.