        if  (a instanceof Double && b instanceof Double) {
            if  ((Double) a < (Double) b) {
                return Optional.of(b);
            } else if  ((Double) a > (Double) b) {
                return Optional.of(a);
            }
        } else if  (a instanceof Float && b instanceof Float) {
            if  ((Float) a < (Float) b) {
                return Optional.of(b);
            } else if  ((Float) a > (Float) b) {
                return Optional.of(a);
            }
        } else if  (a instanceof String && b instanceof String) {
            if  (Double.parseDouble((String) a) < Double.parseDouble((String) b)) {
                return Optional.of(b);
            } else if  (Double.parseDouble((String) a) > Double.parseDouble((String) b)) {
                return Optional.of(a);
            }
        } else if  (a instanceof Integer && b instanceof Integer) {
            if  ((Integer) a < (Integer) b) {
                return Optional.of(b);
            } else if  ((Integer) a > (Integer) b) {
                return Optional.of(a);
            }
        } else if  (a instanceof Float && b instanceof Double) {
            if  ((Float) a < (Double) b) {
                return Optional.of(b);
            } else if  ((Float) a > (Double) b) {
                return Optional.of(a);
            }
        } else if  (a instanceof Double && b instanceof Float) {
            if  ((Double) a < (Float) b) {
                return Optional.of(b);
            } else if  ((Double) a > (Float) b) {
                return Optional.of(a);
            }
        } else if  (a instanceof Integer && b instanceof Float) {
            if  ((Integer) a < (Float) b) {
                return Optional.of(b);
            } else if  ((Integer) a > (Float) b) {
                return Optional.of(a);
            }
        } else if  (