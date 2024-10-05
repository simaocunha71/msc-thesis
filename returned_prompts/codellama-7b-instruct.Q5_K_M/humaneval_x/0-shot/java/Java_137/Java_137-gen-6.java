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
        if (a instanceof Double || b instanceof Double) {
            return Optional.of(Math.max(toDouble(a), toDouble(b)));
        } else if (a instanceof Float || b instanceof Float) {
            return Optional.of(Math.max(toFloat(a), toFloat(b)));
        } else {
            return Optional.of(Math.max(toInt(a), toInt(b)));
        }
    }

    private double toDouble(Object a) {
        if (a instanceof String) {
            return Double.parseDouble((String) a);
        } else if (a instanceof Double) {
            return (Double) a;
        } else if (a instanceof Float) {
            return (Float) a;
        }

        throw new IllegalArgumentException();
    }

    private float toFloat(Object a) {
        if (a instanceof String) {
            return Float.parseFloat((String) a);
        } else if (a instanceof Float) {
            return (Float) a;
        } else if (a instanceof Double) {
            return (float) (Double) a;
        }

        throw new IllegalArgumentException();
    }

    private int toInt(Object a) {
        if (a instanceof String) {
            return Integer.parseInt((String) a);
        } else if (a instanceof Integer) {
            return (int) a;
        }