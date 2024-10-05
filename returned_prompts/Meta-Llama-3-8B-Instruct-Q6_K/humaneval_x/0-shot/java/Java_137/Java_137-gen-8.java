```java
import java.util.*;
import java.lang.*;

class Solution {
    public Optional<Object> compareOne(Object a, Object b) {
        if (a instanceof Integer && b instanceof Integer) {
            if ((int) a > (int) b) {
                return Optional.of(a);
            } else if ((int) a < (int) b) {
                return Optional.of(b);
            } else {
                return Optional.empty();
            }
        } else if (a instanceof Float && b instanceof Float) {
            if ((float) a > (float) b) {
                return Optional.of(a);
            } else if ((float) a < (float) b) {
                return Optional.of(b);
            } else {
                return Optional.empty();
            }
        } else if (a instanceof String && b instanceof String) {
            String strA = (String) a;
            String strB = (String) b;
            strA = strA.replace(",", "");
            strB = strB.replace(",", "");
            if (Float.parseFloat(strA) > Float.parseFloat(strB)) {
                return Optional.of(a);
            } else if (Float.parseFloat(strA) < Float.parseFloat(strB)) {
                return Optional.of(b);
            } else {
                return Optional.empty();
            }
        } else {
            throw new RuntimeException("Invalid input types");
        }
    }
}
```
