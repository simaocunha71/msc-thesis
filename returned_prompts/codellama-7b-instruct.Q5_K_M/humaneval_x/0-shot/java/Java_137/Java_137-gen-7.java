        if (a instanceof Float || b instanceof Float) {
            return Optional.ofNullable(Math.max(
                    ((Float) a).doubleValue(),
                    ((Float) b).doubleValue()));
        }

B:
        if (a instanceof Double || b instanceof Double) {
            return Optional.ofNullable(Math.max(
                    ((Double) a).doubleValue(),
                    ((Double) b).doubleValue()));
        }

C:
        if (a instanceof Integer || b instanceof Integer) {
            return Optional.ofNullable(Math.max(
                    ((Integer) a).intValue(),
                    ((Integer) b).intValue()));
        }

D:
        if (a instanceof String || b instanceof String) {
            if (a instanceof String && b instanceof String) {
                return Optional.ofNullable(
                        (((String) a).compareTo((String) b) > 0) ? a : b);
            } else {
                return Optional.ofNullable(
                        (((String) a).compareTo(String.valueOf(b)) > 0) ? a : b);
            }
        }

        return Optional.empty();
    }
}
