        if (a instanceof Integer && b instanceof Integer) {
            return (int) a > (int) b ? Optional.of((int) a) : Optional.empty();

        } else if (a instanceof Float && b instanceof Float) {
            return (float) a > (float) b ? Optional.of((float) a) : Optional.empty();

        } else if (a instanceof Double && b instanceof Double) {
            return (double) a > (double) b ? Optional.of((double) a) : Optional.empty();

        } else if (a instanceof String && b instanceof String) {
            return ((String) a).compareTo((String) b) > 0 ? Optional.of((String) a) : Optional.empty();

        } else if (a instanceof Integer && b instanceof Float) {
            return (int) a > (float) b ? Optional.of((int) a) : Optional.empty();

        } else if (a instanceof Integer && b instanceof Double) {
            return (int) a > (double) b ? Optional.of((int) a) : Optional.empty();

        } else if (a instanceof Float && b instanceof Integer) {
            return (float) a > (int) b ? Optional.of((float) a) : Optional.empty();

        } else if (a instanceof Float && b instanceof Double) {
            return (float) a > (double) b ? Optional.of((float) a) : Optional.empty();

        } else if (a instanceof Double && b instanceof Integer) {
            return (double) a > (int) b ? Optional.of((double) a) : Optional.empty();

        } else if (a instanceof Double && b instanceof Float) {
            return (double) a > (float) b ? Optional.of((double) a) : Optional.empty();

        } else if (a instanceof String && b instanceof Integer) {
            return ((String) a).compareTo("" + (int) b) > 0 ? Optional.of((String) a) : Optional.empty();

        } else if (a instanceof String && b instanceof Float) {
            return ((String) a).compareTo("" + (float) b) > 0 ? Optional