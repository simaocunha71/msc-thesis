```java
import java.util.*;

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
            String astr = (String) a;
            String bstr = (String) b;
            astr = astr.replace(",", ".");
            bstr = bstr.replace(",", ".");
            if (Float.parseFloat(astr) > Float.parseFloat(bstr)) {
                return Optional.of(a);
            } else if (Float.parseFloat(astr) < Float.parseFloat(bstr)) {
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


This solution first checks if both inputs are integers. If so, it compares them and returns the larger one. If they are equal, it returns an empty optional.

If both inputs are not integers, it checks if they are floats. If so, it compares them and returns the larger one. If they are equal, it returns an empty optional.

If both inputs are not floats, it checks if they are strings. If so, it converts the strings to floats (after replacing any commas with dots), compares them, and returns the larger one. If they are equal, it returns an empty optional.

If none of the above conditions are met, it returns an empty optional. 

This solution assumes that if a string represents a real number, it will be in the format of ". or ,". It also assumes that the inputs are either integers, floats, or strings representing real numbers. If the inputs are not in this format, the behavior of the function is undefined. 

The function returns an Optional of the larger value, or an empty Optional if the values are equal. 

The function uses the Optional class from the Java Util library, which is used to represent a container which may or may