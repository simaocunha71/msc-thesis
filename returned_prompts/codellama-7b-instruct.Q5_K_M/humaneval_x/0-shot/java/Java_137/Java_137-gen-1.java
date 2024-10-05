import java.util.*;
import java.lang.*;

class Solution {
    /**
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compareOne(1, 2.5) -> Optional.of(2.5)
    compareOne(1, "2,3") -> Optional.of("2,3")
    compareOne("5,1", "6") -> Optional.of("6")
    compareOne("1", 1) -> Optional.empty()
     */
    public Optional<Object> compareOne(Object a, Object b) {
        if (a instanceof String) {
            // Convert string to double
            double aVal = Double.parseDouble((String) a);
            // Compare the two values
            if (aVal > Double.parseDouble((String) b)) {
                return Optional.of(a);
            } else if (aVal < Double.parseDouble((String) b)) {
                return Optional.of(b);
            } else {
                return Optional.empty();
            }
        } else if (a instanceof Integer || a instanceof Double || a instanceof Float) {
            // Compare the two values
            if (a > b) {
                return Optional.of(a);
            } else if (a < b) {
                return Optional.of(b);
            } else {
                return Optional.empty();
            }
        } else {
            return Optional.empty();
        }
    }
}
