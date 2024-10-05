        if (a instanceof Integer && b instanceof Integer) {
            return Optional.of(Math.max(a, b));
        } else if (a instanceof Float && b instanceof Float) {
            return Optional.of(Math.max(a, b));
        } else if (a instanceof Double && b instanceof Double) {
            return Optional.of(Math.max(a, b));
        } else if (a instanceof String && b instanceof String) {
            if (((String) a).equals(((String) b))) return Optional.empty();
            if (b instanceof Integer) {
                return ((String) a).startsWith(".") ?
                    Optional.of(b) :
                    Optional.of(((String) a));
            } else if (b instanceof Float) {
                return ((String) a).startsWith(".") ?
                    Optional.of(b) :
                    Optional.of(((String) a));
            } else if (b instanceof Double) {
                return ((String) a).startsWith(".") ?
                    Optional.of(b) :
                    Optional.of(((String) a));
            } else if (b instanceof String) {
                if (((String) a).equals(((String) b))) return Optional.empty();
                if (((String) b).startsWith(".")) return Optional.of(((String) a));
                return Optional.of(((String) b));
            }
        }
        return Optional.empty();
    }
}

