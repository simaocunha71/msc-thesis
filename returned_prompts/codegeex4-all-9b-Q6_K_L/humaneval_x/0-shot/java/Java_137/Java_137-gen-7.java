```java
import java.util.*;
import java.lang.*;

class Solution {
    public Optional<Object> compareOne(Object a, Object b) {
        if (a instanceof String && b instanceof String) {
            if (a.equals(b)) return Optional.empty();
            else {
                String aStr = ((String) a).replace(',', '.');
                String bStr = ((String) b).replace(',', '.');
                double aDouble = Double.parseDouble(aStr);
                double bDouble = Double.parseDouble(bStr);
                if (aDouble > bDouble) return Optional.of(a);
                else return Optional.of(b);
            }
        } else if (a instanceof String) {
            String aStr = ((String) a).replace(',', '.');
            double aDouble = Double.parseDouble(aStr);
            if (aDouble > (Double) b) return Optional.of(a);
            else return Optional.of(b);
        } else if (b instanceof String) {
            String bStr = ((String) b).replace(',', '.');
            double bDouble = Double.parseDouble(bStr);
            if ((Double) a > bDouble) return Optional.of(a);
            else return Optional.of(b);
        } else if (a instanceof Double && b instanceof Double) {
            if ((Double) a == (Double) b) return Optional.empty();
            else if ((Double) a > (Double) b) return Optional.of(a);
            else return Optional.of(b);
        } else if (a instanceof Double) {
            if ((Double) a > (Double) b) return Optional.of(a);
            else return Optional.of(b);
        } else if (b instanceof Double) {
            if ((Double) a < (Double) b) return Optional.of(b);
            else return Optional.of(a);
        } else return Optional.empty();
    }
}
```