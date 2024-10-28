import java.util.*;

class Solution {
    public Optional<Object> compareOne(Object a, Object b) {
        // If both objects are of the same type, compare them directly
        if (a.getClass().equals(b.getClass())) {
            if (a instanceof Comparable) {
                return ((Comparable) a).compareTo(b) > 0 ? Optional.of(a) : Optional.of(b);
            }
        } else {
            // If objects are not of the same type, compare them as strings
            String aStr = a.toString();
            String bStr = b.toString();
            if (aStr.compareTo(bStr) > 0) {
                return Optional.of(a);
            } else if (aStr.compareTo(bStr) < 0) {
                return Optional.of(b);
            }
        }
        return Optional.empty();
    }
}