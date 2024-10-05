        if (a instanceof Integer && b instanceof Integer) {
            if ((int) a == (int) b) {
                return Optional.empty();
            } else if ((int) a > (int) b) {
                return Optional.of((int) a);
            } else {
                return Optional.of((int) b);
            }
        } else if (a instanceof Double && b instanceof Double) {
            if (Math.abs(a - b) < 1e-10) {
                return Optional.empty();
            } else if (Double.doubleToLongBits(a) > Double.doubleToLongBits(b)) {
                return Optional.of(a);
            } else {
                return Optional.of(b);
            }
        } else if (a instanceof String && b instanceof String) {
            if (a.equals(b)) {
                return Optional.empty();
            } else if (a.toString().equals(Double.toString(b))) {
                return Optional.of(a);
            } else {
                return Optional.of(b);
            }
        } else if (a instanceof Integer && b instanceof Float) {
            if (Double.doubleToLongBits(a) > Double.doubleToLongBits(b)) {
                return Optional.of(a);
            } else {
                return Optional.of(b);
            }
        } else if (a instanceof Float && b instanceof Integer) {
            if (Double.doubleToLongBits(a) > Double.doubleToLongBits(b)) {
                return Optional.of(a);
            } else {
                return Optional.of(b);
            }
        } else if (a instanceof Double && b instanceof Integer) {
            if (Double.doubleToLongBits(a) > Double.doubleToLongBits(b)) {
                return Optional.of(a);
            } else {
                return Optional.of(b);
            }
        } else if (a instanceof Integer && b instanceof Float) {
            if (Double.doubleToLongBits(a) > Double.doubleToLongBits(b)) {
                return Optional.of(a);
