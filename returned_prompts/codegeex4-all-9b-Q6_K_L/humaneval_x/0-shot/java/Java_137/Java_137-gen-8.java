```java
import java.util.*;
import java.lang.*;

class Solution {
    public Optional<Object> compareOne(Object a, Object b) {
        if (a instanceof String) {
            a = Double.parseDouble((String) a.replace(',', '.'));
        }
        if (b instanceof String) {
            b = Double.parseDouble((String) b.replace(',', '.'));
        }
        if (a instanceof Double && b instanceof Double) {
            if ((Double) a > (Double) b) {
                return Optional.of(a);
            } else if ((Double) a < (Double) b) {
                return Optional.of(b);
            } else {
                return Optional.empty();
            }
        } else if (a instanceof Double) {
            return Optional.of(a);
        } else if (b instanceof Double) {
            return Optional.of(b);
        } else {
            return Optional.empty();
        }
    }
}
```