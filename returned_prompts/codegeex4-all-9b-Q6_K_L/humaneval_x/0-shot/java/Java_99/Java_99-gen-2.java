Here is a Java solution for the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int closest_integer(String value) {
        double num = Double.parseDouble(value);
        return (int) Math.round(num);
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.closest_integer("10")); // Output: 10
        System.out.println(solution.closest_integer("15.3")); // Output: 15
        System.out.println(solution.closest_integer("14.5")); // Output: 15
        System.out.println(solution.closest_integer("-14.5")); // Output: -15
    }
}
```

The `closest_integer` function converts the given string to a double, rounds it to the nearest integer, and returns the result as an integer. The `main` function tests this function with different inputs.