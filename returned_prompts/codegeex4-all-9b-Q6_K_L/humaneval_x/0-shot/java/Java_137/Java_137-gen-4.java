```java
import java.util.*;
import java.lang.*;

class Solution {
    public Optional<Object> compareOne(Object a, Object b) {
        if (a instanceof String && b instanceof String) {
            String s1 = ((String) a).replace(',', '.');
            String s2 = ((String) b).replace(',', '.');
            if (Double.parseDouble(s1) == Double.parseDouble(s2)) {
                return Optional.empty();
            }
            return Double.parseDouble(s1) > Double.parseDouble(s2) ? Optional.of(a) : Optional.of(b);
        }
        if (a instanceof String) {
            String s1 = ((String) a).replace(',', '.');
            if (Double.parseDouble(s1) == ((Double) b)) {
                return Optional.empty();
            }
            return Double.parseDouble(s1) > ((Double) b) ? Optional.of(a) : Optional.of(b);
        }
        if (b instanceof String) {
            String s2 = ((String) b).replace(',', '.');
            if (((Double) a) == Double.parseDouble(s2)) {
                return Optional.empty();
            }
            return ((Double) a) > Double.parseDouble(s2) ? Optional.of(a) : Optional.of(b);
        }
        if (((Double) a) == ((Double) b)) {
            return Optional.empty();
        }
        return ((Double) a) > ((Double) b) ? Optional.of(a) : Optional.of(b);
    }
}
```