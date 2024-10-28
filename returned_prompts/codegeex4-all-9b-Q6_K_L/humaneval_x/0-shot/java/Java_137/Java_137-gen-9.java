```java
import java.util.*;
import java.lang.*;

class Solution {
    public Optional<Object> compareOne(Object a, Object b) {
        Object max = null;
        if (a instanceof Double || b instanceof Double) {
            Double aDouble = (a instanceof Double) ? (Double) a : Double.parseDouble(a.toString().replace(',', '.'));
            Double bDouble = (b instanceof Double) ? (Double) b : Double.parseDouble(b.toString().replace(',', '.'));
            if (aDouble.compareTo(bDouble) > 0) {
                max = a;
            } else if (aDouble.compareTo(bDouble) < 0) {
                max = b;
            }
        } else if (a instanceof Integer || b instanceof Integer) {
            Integer aInt = (a instanceof Integer) ? (Integer) a : Integer.parseInt(a.toString());
            Integer bInt = (b instanceof Integer) ? (Integer) b : Integer.parseInt(b.toString());
            if (aInt.compareTo(bInt) > 0) {
                max = a;
            } else if (aInt.compareTo(bInt) < 0) {
                max = b;
            }
        } else {
            max = (String.valueOf(a).compareTo(String.valueOf(b)) > 0) ? a : b;
        }
        return (max == null || max.equals(b)) ? Optional.empty() : Optional.of(max);
    }
}
```
In this solution, we first check if either `a` or `b` is a `Double` or `Integer`. If so, we parse them into their respective types and compare them. If neither `a` nor `b` is a `Double` or `Integer`, we compare them as strings.

If `max` is `null` or equal to `b`, we return `Optional.empty()`. Otherwise, we return `Optional.of(max)`.