        if (a instanceof Double && b instanceof Double) {
            if (((Double) a).compareTo((Double) b) > 0) {
                return Optional.of(a);
            } else if (((Double) a).compareTo((Double) b) < 0) {
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
        } else if (a instanceof Integer && b instanceof Integer) {
            if ((Integer) a > (Integer) b) {
                return Optional.of(a);
            } else if ((Integer) a < (Integer) b) {
                return Optional.of(b);
            } else {
                return Optional.empty();
            }
        } else {
            throw new ClassCastException("Both objects must be of the same type");
        }
    }
}

