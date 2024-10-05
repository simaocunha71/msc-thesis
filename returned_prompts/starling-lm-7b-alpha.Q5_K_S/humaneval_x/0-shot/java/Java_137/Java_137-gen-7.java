        if (a instanceof Integer && b instanceof Integer) {
            if ((int) a == (int) b) {
                return Optional.empty();
            } else if ((int) a > (int) b) {
                return Optional.of((int) a);
            } else {
                return Optional.of((int) b);
            }
        } else if (a instanceof Integer && b instanceof Float) {
            if ((int) a == (int) Math.floor(b)) {
                return Optional.empty();
            } else if ((int) a > (int) Math.floor(b)) {
                return Optional.of((int) a);
            } else {
                return Optional.of((int) b);
            }
        } else if (a instanceof Integer && b instanceof String) {
            if (a.equals(b)) {
                return Optional.empty();
            } else if (a.toString().equals(b.toString())) {
                return Optional.of((int) a);
            } else {
                return Optional.of((int) b);
            }
        } else if (a instanceof Float && b instanceof Integer) {
            if ((int) Math.floor(a) == (int) b) {
                return Optional.empty();
            } else if ((int) Math.floor(a) > (int) b) {
                return Optional.of((int) Math.floor(a));
            } else {
                return Optional.of((int) b);
            }
        } else if (a instanceof Float && b instanceof Float) {
            if (a == b) {
                return Optional.empty();
            } else if (a > b) {
                return Optional.of(a);
            } else {
                return Optional.of(b);
            }
        } else if (a instanceof Float && b instanceof String) {
            if (a.toString().equals(b.toString())) {
                return Optional.of(a);
            } else {
                return Optional.of(b);
            }
        } else if (a instanceof String && b instanceof Integer) {
            if (a.toString().equals(b