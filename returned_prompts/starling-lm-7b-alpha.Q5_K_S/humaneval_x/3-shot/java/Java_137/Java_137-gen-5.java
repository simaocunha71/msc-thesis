        if (a instanceof Integer && b instanceof Integer) {
            if ((int) a == (int) b) return Optional.empty();
            return Optional.of((int) Math.max(a, b));
        }
        if (a instanceof Float && b instanceof Float) {
            if ((float) a == (float) b) return Optional.empty();
            return Optional.of((float) Math.max(a, b));
        }
        if (a instanceof Double && b instanceof Double) {
            if ((double) a == (double) b) return Optional.empty();
            return Optional.of((double) Math.max(a, b));
        }
        if (a instanceof Integer && b instanceof Float) {
            return Optional.of(Math.max(a, b));
        }
        if (a instanceof Integer && b instanceof Double) {
            return Optional.of(Math.max(a, b));
        }
        if (a instanceof Float && b instanceof Integer) {
            return Optional.of(Math.max(a, b));
        }
        if (a instanceof Float && b instanceof Double) {
            return Optional.of(Math.max(a, b));
        }
        if (a instanceof Double && b instanceof Integer) {
            return Optional.of(Math.max(a, b));
        }
        if (a instanceof Double && b instanceof Float) {
            return Optional.of(Math.max(a, b));
        }
        if (a instanceof String && b instanceof Integer) {
            return Optional.of(Math.max(a, b));
        }
        if (a instanceof String && b instanceof Float) {
            return Optional.of(Math.max(a, b));
        }
        if (a instanceof String && b instanceof Double) {
            return Optional.of(Math.max(a, b));
        }
        if (b instanceof String && a instanceof Integer) {
            return Optional.of(Math.max(a, b));
        }
        if (b instanceof String && a instanceof Float) {
            return Optional.of(Math.max(a, b));
        }
        if (b instanceof String && a instanceof Double) {
            return Optional.of