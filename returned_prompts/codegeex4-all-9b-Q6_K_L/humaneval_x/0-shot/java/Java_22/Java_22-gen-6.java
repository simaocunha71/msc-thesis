Here's how you might write this in Java:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> filterIntegers(List<Object> values) {
        List<Integer> integers = new ArrayList<>();
        for (Object value : values) {
            if (value instanceof Integer) {
                integers.add((Integer) value);
            }
        }
        return integers;
    }
}
```

In this code, we create an empty list of integers. Then, for each value in the input list, we check if it is an instance of Integer. If it is, we add it to our list of integers. Finally, we return our list of integers.

We can test this method with the following code:

```java
public static void main(String[] args) {
    Solution solution = new Solution();
    List<Object> values = Arrays.asList('a', 3.14, 5);
    List<Integer> integers = solution.filterIntegers(values);
    System.out.println(integers); // prints [5]

    values = Arrays.asList(1, 2, 3, "abc", new HashMap<>(), new ArrayList<>());
    integers = solution.filterIntegers(values);
    System.out.println(integers); // prints [1, 2, 3]
}
```

This code creates a new instance of the Solution class, then calls the filterIntegers method with two different lists of values. It prints out the results of each call.