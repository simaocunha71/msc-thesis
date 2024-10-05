        if (a instanceof Integer && b instanceof Integer) {
            if (a.equals(b)) {
                return Optional.empty();
            } else if ((Integer) a > (Integer) b) {
                return Optional.of((Integer) a);
            } else {
                return Optional.of((Integer) b);
            }
        } else if (a instanceof Float && b instanceof Float) {
            if (a.equals(b)) {
                return Optional.empty();
            } else if ((Float) a > (Float) b) {
                return Optional.of((Float) a);
            } else {
                return Optional.of((Float) b);
            }
        } else if (a instanceof String && b instanceof String) {
            if (a.equals(b)) {
                return Optional.empty();
            } else if (a.toString().replaceAll("\\.", "").replaceAll("\\,", ".").compareTo(b.toString().replaceAll("\\.", "").replaceAll("\\,", ".")) > 0) {
                return Optional.of(a);
            } else {
                return Optional.of(b);
            }
        } else {
            return Optional.empty();
        }
    }
}






















































































































































































































