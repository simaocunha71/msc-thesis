        if (a instanceof Integer && b instanceof Integer) {
            return (Integer) a > (Integer) b ? Optional.of(a) : (Integer) a == (Integer) b ? Optional.empty() : Optional.of(b);
        }
        if (a instanceof Float && b instanceof Float) {
            return (Float) a > (Float) b ? Optional.of(a) : (Float) a == (Float) b ? Optional.empty() : Optional.of(b);
        }
        if (a instanceof String && b instanceof String) {
            return Float.parseFloat((String) a) > Float.parseFloat((String) b) ? Optional.of(a) : Float.parseFloat((String) a) == Float.parseFloat((String) b) ? Optional.empty() : Optional.of(b);
        }
        if (a instanceof String && b instanceof Integer) {
            return Float.parseFloat((String) a) > (Integer) b ? Optional.of(a) : Float.parseFloat((String) a) == (Integer) b ? Optional.empty() : Optional.of(b);
        }
        if (a instanceof Integer && b instanceof String) {
            return (Integer) a > Float.parseFloat((String) b) ? Optional.of(a) : (Integer) a == Float.parseFloat((String) b) ? Optional.empty() : Optional.of(b);
        }
        if (a instanceof Float && b instanceof Integer) {
            return (Float) a > (Integer) b ? Optional.of(a) : (Float) a == (Integer) b ? Optional.empty() : Optional.of(b);
        }
        if (a instanceof String && b instanceof Float) {
            return Float.parseFloat((String) a) > (Float) b ? Optional.of(a) : Float.parseFloat((String) a) == (Float) b ? Optional.empty() : Optional.of(b);
        }
        return Optional.empty();
    }
}

Is it correct? I'm not sure about the if condition check for floats and strings.

A: Your code is mostly correct, but there are a few issues