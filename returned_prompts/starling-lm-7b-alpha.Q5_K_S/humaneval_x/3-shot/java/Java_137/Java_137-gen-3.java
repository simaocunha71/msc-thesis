        if (a instanceof Integer && b instanceof Integer) {
            return Optional.of(a instanceof Integer && b instanceof Integer && (Integer) a > (Integer) b ? a : Optional.empty());
        } else if (a instanceof Float && b instanceof Float) {
            return Optional.of(a instanceof Float && b instanceof Float && (Float) a > (Float) b ? a : Optional.empty());
        } else if (a instanceof String && b instanceof String) {
            return Optional.of(a instanceof String && b instanceof String && ((String) a).compareTo((String) b) > 0 ? a : Optional.empty());
        } else if (a instanceof Integer && b instanceof Float) {
            return Optional.of(a instanceof Integer && b instanceof Float && (Integer) a > (Float) b ? a : Optional.empty());
        } else if (a instanceof Float && b instanceof Integer) {
            return Optional.of(a instanceof Float && b instanceof Integer && (Float) a > (Integer) b ? a : Optional.empty());
        } else if (a instanceof String && b instanceof Float) {
            return Optional.of(a instanceof String && b instanceof Float && ((String) a).compareTo(String.valueOf(b)) > 0 ? a : Optional.empty());
        } else if (a instanceof Float && b instanceof String) {
            return Optional.of(a instanceof Float && b instanceof String && String.valueOf(b).compareTo((String) a) > 0 ? a : Optional.empty());
        } else if (a instanceof String && b instanceof String) {
            return Optional.of(a instanceof String && b instanceof String && ((String) a).compareTo((String) b) > 0 ? a : Optional.empty());
        }
        return Optional.empty();
    }

    /**
    Create a function that takes a list of two real numbers, and returns the larger of them.
    Return None if the values are equal.

    compareTwo(1, 2.5) -> Optional.of(2.5)
    compareTwo(1, "2,3") -> Optional.of("2,3")
    compareTwo("5,1", "6") -> Optional.of("6")
    compareTwo("1", 1)