        if (a instanceof Integer && b instanceof Integer) {
            return Integer.compare((Integer) a, (Integer) b) > 0 ?
                Optional.of((Integer) a) : Optional.empty();
        } else if (a instanceof Float && b instanceof Float) {
            return Float.compare((Float) a, (Float) b) > 0 ?
                Optional.of((Float) a) : Optional.empty();
        } else if (a instanceof Double && b instanceof Double) {
            return Double.compare((Double) a, (Double) b) > 0 ?
                Optional.of((Double) a) : Optional.empty();
        } else if (a instanceof String && b instanceof String) {
            return ((String) a).compareTo((String) b) > 0 ?
                Optional.of((String) a) : Optional.empty();
        } else if (a instanceof Integer && b instanceof Float) {
            return Float.compare((Float) b, (Integer) a) > 0 ?
                Optional.of((Float) b) : Optional.empty();
        } else if (a instanceof Integer && b instanceof Double) {
            return Double.compare((Double) b, (Integer) a) > 0 ?
                Optional.of((Double) b) : Optional.empty();
        } else if (a instanceof Integer && b instanceof String) {
            return ((String) b).compareTo((Integer) a) > 0 ?
                Optional.of((String) b) : Optional.empty();
        } else if (a instanceof Float && b instanceof Integer) {
            return Float.compare((Float) b, (Integer) a) > 0 ?
                Optional.of((Float) b) : Optional.empty();
        } else if (a instanceof Float && b instanceof Double) {
            return Double.compare((Double) b, (Float) a) > 0 ?
                Optional.of((Double) b) : Optional.empty();
        } else if (a instanceof Float && b instanceof String) {
            return ((String) b).compareTo((Float) a) > 0 ?
                Optional.of((String) b) : Optional.empty();
        } else if (a instanceof