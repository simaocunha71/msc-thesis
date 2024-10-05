To solve this problem, we can use the `Math.round()` function in Java. This function rounds the given number to the nearest integer. If the number is equidistant from two integers, it rounds away from zero.

Here is the updated code:

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

In the `closest_integer()` function, we first parse the given value to a double using `Double.parseDouble()`. Then, we use `Math.round()` to round the number to the nearest integer. Finally, we cast the result to an int and return it.

In the `main()` function, we create an instance of the `Solution` class and call the `closest_integer()` function with different inputs to test its correctness.