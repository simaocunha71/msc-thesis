        if (a instanceof Integer && b instanceof Integer) {
            if (((Integer) a).equals(((Integer) b))) {
                return Optional.empty();
            } else if (((Integer) a) > ((Integer) b)) {
                return Optional.of(((Integer) a));
            } else {
                return Optional.of(((Integer) b));
            }
        } else if (a instanceof Float && b instanceof Float) {
            if (((Float) a).equals(((Float) b))) {
                return Optional.empty();
            } else if (((Float) a) > ((Float) b)) {
                return Optional.of(((Float) a));
            } else {
                return Optional.of(((Float) b));
            }
        } else if (a instanceof Double && b instanceof Double) {
            if (((Double) a).equals(((Double) b))) {
                return Optional.empty();
            } else if (((Double) a) > ((Double) b)) {
                return Optional.of(((Double) a));
            } else {
                return Optional.of(((Double) b));
            }
        } else if (a instanceof String && b instanceof String) {
            if (((String) a).equals(((String) b))) {
                return Optional.empty();
            } else if (((String) a).compareTo(((String) b)) > 0) {
                return Optional.of(((String) a));
            } else {
                return Optional.of(((String) b));
            }
        } else if (a instanceof Integer && b instanceof Float) {
            if (((Integer) a).equals(((Float) b))) {
                return Optional.empty();
            } else if (((Integer) a) > ((Float) b)) {
                return Optional.of(((Integer) a));
            } else {
                return Optional.of(((Float) b));
            }
        } else if (a instanceof Float && b instanceof Integer) {
            if (((Float) b).equals(((Integer) a))) {
                return Optional.empty();
            } else if (((Float) b) > ((Integer) a)) {
                return Optional.of(((Float) b));
            } else {
               