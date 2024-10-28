    import java.util.*;
    import java.lang.*;

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
                if (compareString((String) a, (String) b) > 0) {
                    return Optional.of(a);
                } else if (compareString((String) a, (String) b) < 0) {
                    return Optional.of(b);
                } else {
                    return Optional.empty();
                }
            } else if (a instanceof Integer && b instanceof Float) {
                return Optional.of(b);
            } else if (a instanceof Float && b instanceof Integer) {
                return Optional.of(b);
            } else if (a instanceof String && b instanceof Integer) {
                return Optional.of(b);
            } else if (a instanceof Integer && b instanceof String) {
                return Optional.of(b);
            } else if (a instanceof Float && b instanceof String) {
                return Optional.of(b);
            } else if (a instanceof String && b instanceof Float) {
                return Optional.of(b);
            }
            return Optional.empty();
        }

        private int compareString(String a, String b) {
            String[] partsA = a.replace(",", "").split("\\.");
            String[] partsB = b.replace(",", "").split("\\.");

            int i = 0;
            while (i < partsA.length && i < partsB.length) {
                int numA = Integer.parseInt(partsA[i]);
                int numB = Integer.parseInt(partsB[i]);
                if (numA > numB) {
                    return 1;
                } else if (numA < numB) {
                    return -1;
                }
                i++;
            }
            if (i < partsA.length) {
                return 1;
            } else if (i < partsB.length)