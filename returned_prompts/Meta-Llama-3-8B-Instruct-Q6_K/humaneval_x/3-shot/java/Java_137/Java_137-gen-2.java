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
            if (parseFloat((String) a) > parseFloat((String) b)) {
                return Optional.of(a);
            } else if (parseFloat((String) a) < parseFloat((String) b)) {
                return Optional.of(b);
            } else {
                return Optional.empty();
            }
        } else if (a instanceof Integer && b instanceof Float) {
            if ((int) a > (float) b) {
                return Optional.of(a);
            } else if ((int) a < (float) b) {
                return Optional.of(b);
            } else {
                return Optional.empty();
            }
        } else if (a instanceof Float && b instanceof Integer) {
            if ((float) a > (int) b) {
                return Optional.of(a);
            } else if ((float) a < (int) b) {
                return Optional.of(b);
            } else {
                return Optional.empty();
            }
        } else if (a instanceof String && b instanceof Float) {
            if (parseFloat((String) a) > (float) b) {
                return Optional.of(a);
            } else if (parseFloat((String) a) < (float) b) {
                return Optional.of(b);
            } else {
                return Optional.empty();
            }
        } else if (a instanceof Float && b instanceof String) {
            if ((float) a > parseFloat((String) b)) {
                return Optional.of(a);
            } else if ((float) a < parseFloat((String) b)) {
                return Optional.of(b);
            } else {
                return Optional.empty();
            }
        }
        return Optional.empty();
    }

    private float parseFloat(String s) {
        s = s.replace(",", ".");
        return Float.parseFloat(s);
    }
}

Q