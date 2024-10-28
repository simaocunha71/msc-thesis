        double a_double = parseDouble(a);
        double b_double = parseDouble(b);

        if (a_double > b_double) {
            return Optional.of(a);
        } else if (a_double < b_double) {
            return Optional.of(b);
        } else {
            return Optional.empty();
        }
    }

    private double parseDouble(Object a) {
        if (a instanceof String) {
            return Double.parseDouble(((String) a).replace(",", "."));
        } else if (a instanceof Double) {
            return (double) a;
        } else if (a instanceof Float) {
            return (double) (float) a;
        } else if (a instanceof Integer) {
            return (double) (int) a;
        } else {
            throw new IllegalArgumentException("Unsupported type: " + a.getClass().getName());
        }
    }
}

