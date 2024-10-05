        if (a instanceof Integer && b instanceof Integer) {
            if (a.equals(b)) {
                return Optional.empty();
            } else {
                return Optional.of(((Integer) a).compareTo((Integer) b) > 0 ? a : b);
            }

        } else if (a instanceof Float && b instanceof Float) {
            if (a.equals(b)) {
                return Optional.empty();
            } else {
                return Optional.of(((Float) a).compareTo((Float) b) > 0 ? a : b);
            }

        } else if (a instanceof Double && b instanceof Double) {
            if (a.equals(b)) {
                return Optional.empty();
            } else {
                return Optional.of(((Double) a).compareTo((Double) b) > 0 ? a : b);
            }
        } else if (a instanceof String && b instanceof String) {
            if (a.equals(b)) {
                return Optional.empty();
            } else {
                return Optional.of(((String) a).compareTo((String) b) > 0 ? a : b);
            }

        } else if (a instanceof Integer && b instanceof Float) {
            return Optional.of(((Integer) a).doubleValue() > ((Float) b).doubleValue() ? a : b);
        } else if (a instanceof Integer && b instanceof Double) {
            return Optional.of(((Integer) a).doubleValue() > ((Double) b).doubleValue() ? a : b);
        } else if (a instanceof Float && b instanceof Integer) {
            return Optional.of(((Float) b).doubleValue() > ((Integer) a).doubleValue() ? b : a);
        } else if (a instanceof Float && b instanceof Double) {
            return Optional.of(((Float) b).doubleValue() > ((Double) a).doubleValue() ? b : a);
        } else if (a instanceof Double && b instanceof Integer) {
            return Optional.of(((Double) b).doubleValue() > ((Integer) a).doubleValue() ? b : a);
        } else if (a instanceof Double && b instanceof Float) {
            return Optional.of