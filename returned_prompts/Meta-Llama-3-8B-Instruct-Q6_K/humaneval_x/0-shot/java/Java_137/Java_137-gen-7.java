```java
import java.util.*;

class Solution {
    public Optional<Object> compareOne(Object a, Object b) {
        if(a instanceof Integer && b instanceof Integer) {
            int ai = (int) a;
            int bi = (int) b;
            return Optional.of(Math.max(ai, bi));
        } else if(a instanceof Float && b instanceof Float) {
            float af = (float) a;
            float bf = (float) b;
            return Optional.of(Math.max(af, bf));
        } else if(a instanceof String && b instanceof String) {
            String as = (String) a;
            String bs = (String) b;
            as = as.replace(",", ".");
            bs = bs.replace(",", ".");
            float af = Float.parseFloat(as);
            float bf = Float.parseFloat(bs);
            return Optional.of(af > bf ? as : bs);
        } else {
            return Optional.empty();
        }
    }
}
``` 