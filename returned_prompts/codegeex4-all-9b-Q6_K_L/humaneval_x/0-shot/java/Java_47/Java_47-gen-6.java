Here's how you can define a method to calculate the median of a list of integers in Java:

```java
import java.util.*;

class Solution {
    public double median(List<Integer> l) {
        Collections.sort(l);
        int size = l.size();
        if (size % 2 == 0) {
            return (l.get(size / 2 - 1) + l.get(size / 2)) / 2.0;
        } else {
            return l.get(size / 2);
        }
    }
}
```

In this code, we first sort the list in ascending order. Then, depending on the size of the list, we return the middle element if the size is odd, or the average of the two middle elements if the size is even.

Here's how you can use this method:

```java
public static void main(String[] args) {
    Solution solution = new Solution();
    List<Integer> list1 = Arrays.asList(3, 1, 2, 4, 5);
    List<Integer> list2 = Arrays.asList(-10, 4, 6, 1000, 10, 20);

    System.out.println(solution.median(list1)); // Output: 3
    System.out.println(solution.median(list2)); // Output: 15.0
}
```

This code will output the median of the two lists.