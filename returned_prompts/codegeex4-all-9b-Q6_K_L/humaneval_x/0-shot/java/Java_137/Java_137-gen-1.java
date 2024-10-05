```java
import java.util.*;
import java.lang.*;

class Solution {
    public Optional<Object> compareOne(Object a, Object b) {
        if (a instanceof String && b instanceof String) {
            String sa = (String) a;
            String sb = (String) b;
            double da = Double.parseDouble(sa.replace(',', '.'));
            double db = Double.parseDouble(sb.replace(',', '.'));
            if (da > db) {
                return Optional.of(sa);
            } else if (da < db) {
                return Optional.of(sb);
            } else {
                return Optional.empty();
            }
        } else if (a instanceof Number && b instanceof Number) {
            double da = ((Number) a).doubleValue();
            double db = ((Number) b).doubleValue();
            if (da > db) {
                return Optional.of(a);
            } else if (da < db) {
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