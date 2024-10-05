    import java.util.*;
    import java.lang.*;

class Solution {
    public Optional<Object> compareOne(Object a, Object b) {
        if (a instanceof Integer && b instanceof Integer) {
            return Optional.of(((Integer) a).compareTo((Integer) b) > 0 ? a : b);
        } else if (a instanceof Float && b instanceof Float) {
            return Optional.of(((Float) a).compareTo((Float) b) > 0 ? a : b);
        } else if (a instanceof String && b instanceof String) {
            if (((String) a).equals(((String) b))) {
                return Optional.empty();
            } else {
                return Optional.of(((String) a).compareTo(((String) b)) > 0 ? a : b);
            }
        } else {
            return Optional.empty();
        }
    }
}A solution for the problem is:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public Optional<Object> compareOne(Object a, Object b) {
        if (a instanceof Integer && b instanceof Integer) {
            return Optional.of(((Integer) a).compareTo((Integer) b) > 0 ? a : b);
        } else if (a instanceof Float && b instanceof Float) {
            return Optional.of(((Float) a).compareTo((Float) b) > 0 ? a : b);
        } else if (a instanceof String && b instanceof String) {
            if (((String) a).equals(((String) b))) {
                return Optional.empty();
            } else {
                return Optional.of(((String) a).compareTo(((String) b)) > 0 ? a : b);
            }
        } else {
            return Optional.empty();
        }
    }
}
```

This solution uses the Optional class from the java.util package to wrap the result of the comparison. It checks the types of the input objects and performs the comparison accordingly. If the objects are of the same type and equal, it returns an empty Optional. If they are of different types, it returns an empty Optional. If the objects are of the same type and not equal, it returns the larger object wrapped in an Optional. If the objects are of different types, it returns an empty Optional. The comparison is done using the compareTo method for integers and floats, and the compareTo method for strings. The equals method is used to check for equality of strings. The result of the comparison is wrapped in an Optional and returned.