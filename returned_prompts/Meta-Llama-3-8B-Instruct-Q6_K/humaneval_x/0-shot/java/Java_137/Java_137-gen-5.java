```java
import java.util.*;
import java.lang.*;

class Solution {
    public Optional<Object> compareOne(Object a, Object b) {
        if(a instanceof Integer && b instanceof Integer) {
            int intA = (int)a;
            int intB = (int)b;
            if(intA > intB) {
                return Optional.of(a);
            } else if(intA < intB) {
                return Optional.of(b);
            } else {
                return Optional.empty();
            }
        } else if(a instanceof Float && b instanceof Float) {
            float floatA = (float)a;
            float floatB = (float)b;
            if(floatA > floatB) {
                return Optional.of(a);
            } else if(floatA < floatB) {
                return Optional.of(b);
            } else {
                return Optional.empty();
            }
        } else if(a instanceof String && b instanceof String) {
            String strA = (String)a;
            String strB = (String)b;
            if(strA.compareTo(strB) > 0) {
                return Optional.of(a);
            } else if(strA.compareTo(strB) < 0) {
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
The function `compareOne` takes two objects `a` and `b` as input. It first checks if both objects are of the same type using the `instanceof` keyword. If they are both integers, it compares them and returns the larger one as an optional. If they are both floats, it compares them and returns the larger one as an optional. If they are both strings, it compares them using the `compareTo` method and returns the larger one as an optional.

If the objects are of different types, it throws a `ClassCastException` because the function is not designed to handle such a situation.

If the objects are equal, it returns an empty optional. If the objects are not comparable (for example, one is an integer and the other is a string), it will throw a `ClassCastException`.

The function returns an optional object, which is a container that may or may not contain a value. If the function returns an empty optional, it means that the input values are equal. If the function returns a non-empty optional, it contains the larger value. The `Optional` class is part of the Java Standard Library and is used to