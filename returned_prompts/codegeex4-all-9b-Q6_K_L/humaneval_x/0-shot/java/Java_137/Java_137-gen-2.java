```java
import java.util.*;
import java.lang.*;

class Solution {
    public Optional<Object> compareOne(Object a, Object b) {
        if (a instanceof String && b instanceof String) {
            String aStr = (String) a;
            String bStr = (String) b;
            if (aStr.contains(",") || bStr.contains(",")) {
                aStr = aStr.replace(",", ".");
                bStr = bStr.replace(",", ".");
            }
            double aDouble = Double.parseDouble(aStr);
            double bDouble = Double.parseDouble(bStr);
            if (aDouble > bDouble) {
                return Optional.of(a);
            } else if (aDouble < bDouble) {
                return Optional.of(b);
            } else {
                return Optional.empty();
            }
        } else if (a instanceof Number && b instanceof Number) {
            double aDouble = ((Number) a).doubleValue();
            double bDouble = ((Number) b).doubleValue();
            if (aDouble > bDouble) {
                return Optional.of(a);
            } else if (aDouble < bDouble) {
                return Optional.of(b);
            } else {
                return Optional.empty();
            }
        } else {
            return Optional.empty();
        }
    }
}
```

Explanation:
1. The function `compareOne` takes two objects `a` and `b` as input.
2. If both objects are strings, we check if they contain a comma. If they do, we replace the comma with a dot and parse them as double values.
3. If both objects are numbers, we convert them to double values.
4. We compare the values of `a` and `b`. If `a` is greater than `b`, we return `a`. If `a` is less than `b`, we return `b`. If `a` is equal to `b`, we return `Optional.empty()`.
5. If either `a` or `b` is not a number or a string, we return `Optional.empty()`.