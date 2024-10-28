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
            String strA = a.toString().replace(",", ".");
            String strB = b.toString().replace(",", ".");
            if (Double.parseDouble(strA) > Double.parseDouble(strB)) {
                return Optional.of(a);
            } else if (Double.parseDouble(strA) < Double.parseDouble(strB)) {
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
            String strA = a.toString().replace(",", ".");
            if (Double.parseDouble(strA) > (float) b) {
                return Optional.of(a);
            } else if (Double.parseDouble(strA) < (float) b) {
                return Optional.of(b);
            } else {
                return Optional.empty();
            }
        } else if (a instanceof Float && b instanceof String) {
            String strB = b.toString().replace(",", ".");
            if ((float) a > Double.parseDouble(strB)) {
                return Optional.of(a);
            } else if ((float) a < Double.parseDouble(strB)) {
                return Optional.of(b);
            } else {
                return Optional.empty();
            }
        }
        return Optional.empty();
