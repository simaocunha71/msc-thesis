        if (a instanceof Integer && b instanceof Integer) {
            if (((Integer) a).intValue() == ((Integer) b).intValue()) {
                return Optional.empty();
            } else if (((Integer) a).intValue() > ((Integer) b).intValue()) {
                return Optional.of(b);
            } else {
                return Optional.of(a);
            }
        } else if (a instanceof Double && b instanceof Double) {
            if (((Double) a).doubleValue() == ((Double) b).doubleValue()) {
                return Optional.empty();
            } else if (((Double) a).doubleValue() > ((Double) b).doubleValue()) {
                return Optional.of(b);
            } else {
                return Optional.of(a);
            }
        } else if (a instanceof String && b instanceof String) {
            if (((String) a).equals(((String) b))) {
                return Optional.empty();
            } else if (((String) a).compareTo(((String) b)) > 0) {
                return Optional.of(b);
            } else {
                return Optional.of(a);
            }
        } else if (a instanceof Integer && b instanceof String) {
            if (((Integer) a).intValue() == ((String) b).length()) {
                return Optional.empty();
            } else if (((Integer) a).intValue() > ((String) b).length()) {
                return Optional.of(b);
            } else {
                return Optional.of(a);
            }
        } else if (a instanceof String && b instanceof Integer) {
            if (((String) a).length() == ((Integer) b).intValue()) {
                return Optional.empty();
            } else if (((String) a).length() > ((Integer) b).intValue()) {
                return Optional.of(b);
            } else {
                return Optional.of(a);
            }
        } else if (a instanceof Double && b instanceof String) {
            double a_d = Double.parseDouble(a.toString());
            if (((Double) a_d).doubleValue() == ((String) b).length