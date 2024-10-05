```java
import java.util.*;

public class Solution {
    public Optional<Object> compareOne(Object a, Object b) {
        if(a instanceof Integer && b instanceof Integer) {
            if((int)a > (int)b) {
                return Optional.of(a);
            } else if((int)a < (int)b) {
                return Optional.of(b);
            } else {
                return Optional.empty();
            }
        } else if(a instanceof Float && b instanceof Float) {
            if((float)a > (float)b) {
                return Optional.of(a);
            } else if((float)a < (float)b) {
                return Optional.of(b);
            } else {
                return Optional.empty();
            }
        } else if(a instanceof String && b instanceof String) {
            if(((String)a).replace(",", "").compareTo(((String)b).replace(",", "")) > 0) {
                return Optional.of(a);
            } else if(((String)a).replace(",", "").compareTo(((String)b).replace(",", "")) < 0) {
                return Optional.of(b);
            } else {
                return Optional.empty();
            }
        } else {
            throw new ClassCastException("Invalid types");
        }
    }
}
```

Explanation:
The given problem is asking to create a method that takes two objects, compares them, and returns the larger one. If the values are equal, it returns an empty optional. The objects can be of type int, float, or string, representing real numbers.

The method first checks if both objects are of the same type. If they are integers, it compares them directly. If they are floats, it also compares them directly. If they are strings, it removes the commas from the strings and then compares them.

If the objects are of different types, it throws a ClassCastException, as the problem statement does not specify what to do in this case.

The method uses Optional to handle the case where the values are equal, returning an empty optional in this case. The Optional class is a container that may or may not contain a non-null value. It is used to represent a value that may be absent. In this case, the value is absent when the two input values are equal.