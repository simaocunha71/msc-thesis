        if (a instanceof Integer && b instanceof Integer) {
            return Optional.of(Math.max(a, b));
        } else if (a instanceof Integer && b instanceof Double) {
            return Optional.of(Math.max(a, b));
        } else if (a instanceof Double && b instanceof Integer) {
            return Optional.of(Math.max(a, b));
        } else if (a instanceof Double && b instanceof Double) {
            return Optional.of(Math.max(a, b));
        } else if (a instanceof String && b instanceof Integer) {
            return Optional.of(Math.max(a, b));
        } else if (a instanceof Integer && b instanceof String) {
            return Optional.of(Math.max(a, b));
        } else if (a instanceof String && b instanceof String) {
            double a_num = Double.parseDouble(a.toString());
            double b_num = Double.parseDouble(b.toString());

            return Optional.of(Math.max(a_num, b_num));
        } else if (a instanceof Double && b instanceof String) {
            double b_num = Double.parseDouble(b.toString());
            return Optional.of(Math.max(a, b_num));
        } else if (a instanceof String && b instanceof Double) {
            double a_num = Double.parseDouble(a.toString());
            return Optional.of(Math.max(a_num, b));
        } else {
            throw new IllegalArgumentException("Incompatible types");
        }
    }
}

