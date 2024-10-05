        if (a instanceof Integer && b instanceof Integer) {
            if ((int) a == (int) b) {
                return Optional.empty();
            } else if ((int) a > (int) b) {
                return Optional.of(a);
            } else {
                return Optional.of(b);
            }
        } else if (a instanceof Float && b instanceof Float) {
            if ((float) a == (float) b) {
                return Optional.empty();
            } else if ((float) a > (float) b) {
                return Optional.of(a);
            } else {
                return Optional.of(b);
            }
        } else if (a instanceof Double && b instanceof Double) {
            if ((double) a == (double) b) {
                return Optional.empty();
            } else if ((double) a > (double) b) {
                return Optional.of(a);
            } else {
                return Optional.of(b);
            }
        } else if (a instanceof String && b instanceof String) {
            if (a.equals(b)) {
                return Optional.empty();
            } else if (((String) a).compareTo((String) b) > 0) {
                return Optional.of(a);
            } else {
                return Optional.of(b);
            }
        } else {
            return Optional.empty();
        }

    }

    /**
    Create a function that takes a string with a comma-separated list of real numbers
    and returns a comma-separated list of the largest numbers in the same format.
    If the numbers are equal, it should only include one of them.
    Note: The largest number can be in any of the following formats:
    integer, float, or string with a dot or comma as the decimal separator.

    largestRealNumbers("1,2,3") -> "3"
    largestRealNumbers("1,2.5,3.2") -> "3,2.5"
    largestRealNumbers("1.2,3.5,2") -> "3,5"
    largestRealNumbers("