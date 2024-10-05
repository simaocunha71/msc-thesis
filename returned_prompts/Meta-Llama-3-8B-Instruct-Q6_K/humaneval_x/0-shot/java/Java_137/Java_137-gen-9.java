```java
import java.util.*;

class Solution {
    public Optional<Object> compareOne(Object a, Object b) {
        if (a instanceof Integer && b instanceof Integer) {
            int intA = (int) a;
            int intB = (int) b;
            return (intA > intB) ? Optional.of(a) : (intA < intB) ? Optional.of(b) : Optional.empty();
        } else if (a instanceof Float && b instanceof Float) {
            float floatA = (float) a;
            float floatB = (float) b;
            return (floatA > floatB) ? Optional.of(a) : (floatA < floatB) ? Optional.of(b) : Optional.empty();
        } else if (a instanceof String && b instanceof String) {
            String strA = (String) a;
            String strB = (String) b;
            return (strA.compareTo(strB) > 0) ? Optional.of(a) : (strA.compareTo(strB) < 0) ? Optional.of(b) : Optional.empty();
        } else {
            return Optional.empty();
        }
    }
}
```