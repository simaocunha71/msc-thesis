```java
import java.util.*;
import java.lang.*;

class Solution {
    public Optional<Object> compareOne(Object a, Object b) {
        if (a instanceof String) {
            a = ((String) a).replace(',', '.');
        }
        if (b instanceof String) {
            b = ((String) b).replace(',', '.');
        }
        if (a instanceof Double && b instanceof Double) {
            if ((Double) a == (Double) b) {
                return Optional.empty();
            }
            return Optional.of(((Double) a > (Double) b) ? a : b);
        }
        return Optional.empty();
    }
}
```