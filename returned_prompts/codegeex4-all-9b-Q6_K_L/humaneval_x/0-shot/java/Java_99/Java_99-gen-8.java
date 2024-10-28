Here is a solution in Java:

```java
public class Solution {
    public static int closest_integer(String value) {
        double num = Double.parseDouble(value);
        return (int) Math.round(num);
    }
}
```
In this solution, we first convert the string input to a double. We then use the `Math.round` function to round the number to the nearest integer, and finally cast it to an int to remove any decimal places.