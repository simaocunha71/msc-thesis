        if (a instanceof Integer && b instanceof Integer) {
            return Optional.of(Math.max(a, b));
        } else if (a instanceof Float && b instanceof Float) {
            return Optional.of(Math.max(a, b));
        } else if (a instanceof Double && b instanceof Double) {
            return Optional.of(Math.max(a, b));
        } else if (a instanceof Long && b instanceof Long) {
            return Optional.of(Math.max(a, b));
        } else if (a instanceof String && b instanceof String) {
            if (((String) a).equals(((String) b))) {
                return Optional.empty();
            } else if (((String) a).contains(".") && !((String) b).contains(".")) {
                return Optional.of(((String) b));
            } else if (((String) a).contains(",") && !((String) b).contains(",")) {
                return Optional.of(((String) b));
            } else {
                String[] a_parts = ((String) a).split("\\.");
                String[] b_parts = ((String) b).split("\\.");
                if (a_parts.length > 1 && b_parts.length > 1) {
                    if (Integer.parseInt(a_parts[1]) > Integer.parseInt(b_parts[1])) {
                        return Optional.of(a);
                    } else {
                        return Optional.of(b);
                    }
                } else if (a_parts.length > 1 && b_parts.length == 1) {
                    return Optional.of(((String) a));
                } else if (a_parts.length == 1 && b_parts.length > 1) {
                    return Optional.of(((String) b));
                } else {
                    if (Double.parseDouble(((String) a)) > Double.parseDouble(((String) b))) {
                        return Optional.of(a);
                    } else {
                        return Optional.of(b);
                    }
                }
            }
        } else if (a instanceof BigDecimal && b instanceof BigDecimal) {
