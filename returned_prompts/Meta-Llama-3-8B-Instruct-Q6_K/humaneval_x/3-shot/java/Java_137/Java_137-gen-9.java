        if (a instanceof Integer && b instanceof Integer) {
            if ((Integer) a > (Integer) b) {
                return Optional.of(a);
            } else if ((Integer) a < (Integer) b) {
                return Optional.of(b);
            } else {
                return Optional.empty();
            }
        } else if (a instanceof Double && b instanceof Double) {
            if ((Double) a > (Double) b) {
                return Optional.of(a);
            } else if ((Double) a < (Double) b) {
                return Optional.of(b);
            } else {
                return Optional.empty();
            }
        } else if (a instanceof String && b instanceof String) {
            if (Double.parseDouble(((String) a).replace(",", ".")) > Double.parseDouble(((String) b).replace(",", "."))) {
                return Optional.of(a);
            } else if (Double.parseDouble(((String) a).replace(",", ".")) < Double.parseDouble(((String) b).replace(",", "."))) {
                return Optional.of(b);
            } else {
                return Optional.empty();
            }
        } else if (a instanceof Integer && b instanceof Double) {
            if ((Integer) a > (Double) b) {
                return Optional.of(a);
            } else if ((Integer) a < (Double) b) {
                return Optional.of(b);
            } else {
                return Optional.empty();
            }
        } else if (a instanceof Double && b instanceof Integer) {
            if ((Double) a > (Integer) b) {
                return Optional.of(a);
            } else if ((Double) a < (Integer) b) {
                return Optional.of(b);
            } else {
                return Optional.empty();
            }
        } else if (a instanceof String && b instanceof Double) {
            if (Double.parseDouble(((String) a).replace(",", ".")) > (Double) b) {
                return Optional.of(a);
            } else if (Double.parseDouble(((String) a).replace(",", ".")) < (Double) b) {
                return Optional.of(b);
            } else {
                return Optional.empty();
            }
        } else if (a instanceof Double && b instanceof String) {
            if ((Double) a > Double.parseDouble(((String) b).replace(",", "."))) {
                return Optional.of(a);
            } else if ((Double) a < Double.parseDouble(((String) b).replace(",", "."))) {
                return Optional.of(b);
            } else {
                return Optional.empty();
            }
        } else