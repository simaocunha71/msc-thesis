        if (a instanceof Integer && b instanceof Integer) {
            return Optional.of(Math.max(a, b));
        } else if (a instanceof Double && b instanceof Double) {
            return Optional.of(Math.max(a, b));
        } else if (a instanceof Float && b instanceof Float) {
            return Optional.of(Math.max(a, b));
        } else if (a instanceof String && b instanceof String) {
            Double d1 = Double.parseDouble(a.toString());
            Double d2 = Double.parseDouble(b.toString());
            if (d1.equals(d2)) return Optional.empty();
            return Optional.of(d1 < d2 ? b : a);
        } else if (a instanceof String && b instanceof Integer) {
            Double d1 = Double.parseDouble(a.toString());
            return Optional.of(d1 < b ? b : a);
        } else if (a instanceof String && b instanceof Float) {
            Double d1 = Double.parseDouble(a.toString());
            return Optional.of(d1 < b ? b : a);
        } else if (a instanceof String && b instanceof Double) {
            Double d1 = Double.parseDouble(a.toString());
            return Optional.of(d1 < b ? b : a);
        } else if (a instanceof Integer && b instanceof String) {
            Double d1 = Double.parseDouble(b.toString());
            return Optional.of(d1 < a ? b : a);
        } else if (a instanceof Float && b instanceof String) {
            Double d1 = Double.parseDouble(b.toString());
            return Optional.of(d1 < a ? b : a);
        } else if (a instanceof Double && b instanceof String) {
            Double d1 = Double.parseDouble(b.toString());
            return Optional.of(d1 < a ? b : a);
        } else if (a instanceof Float && b instanceof Integer) {
            return Optional.of(b < a ? b : a);
        } else if (a instanceof Float && b instanceof Float) {
            return Optional.of(Math.max(a, b));
        }
        return Optional.empty();