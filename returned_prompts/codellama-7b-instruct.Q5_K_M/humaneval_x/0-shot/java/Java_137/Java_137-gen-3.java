        if (a instanceof Integer && b instanceof Integer) {
            return Optional.ofNullable(compareInt((Integer) a, (Integer) b));
        } else if (a instanceof Double && b instanceof Double) {
            return Optional.ofNullable(compareDouble((Double) a, (Double) b));
        } else if (a instanceof String && b instanceof String) {
            return Optional.ofNullable(compareString((String) a, (String) b));
        } else if (a instanceof Integer && b instanceof Double) {
            return Optional.ofNullable(compareIntDouble((Integer) a, (Double) b));
        } else if (a instanceof Double && b instanceof Integer) {
            return Optional.ofNullable(compareIntDouble((Integer) b, (Double) a));
        } else if (a instanceof String && b instanceof Double) {
            return Optional.ofNullable(compareStringDouble((String) a, (Double) b));
        } else if (a instanceof String && b instanceof Integer) {
            return Optional.ofNullable(compareStringDouble((String) a, (Integer) b));
        } else if (a instanceof Double && b instanceof String) {
            return Optional.ofNullable(compareStringDouble((String) b, (Double) a));
        } else if (a instanceof Integer && b instanceof String) {
            return Optional.ofNullable(compareStringDouble((String) b, (Integer) a));
        }

        return Optional.empty();
    }

    private Double compareDouble(Double a, Double b) {
        if (a > b) {
            return a;
        } else if (a < b) {
            return b;
        } else {
            return null;
        }
    }

    private Double compareIntDouble(Integer a, Double b) {
        Double d = (double) a;
        return compareDouble(d, b);
    }

    private Double compareStringDouble(String a, Double b) {
        Double d = Double.parseDouble(a);
        return compareDouble(d, b);
    }

    private Double compareStringDouble(String a, Integer b) {
        Double d = (double) b;
        return compare