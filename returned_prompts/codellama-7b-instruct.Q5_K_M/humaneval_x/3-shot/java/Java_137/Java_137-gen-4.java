        if (a instanceof Double) {
            Double a_double = (Double) a;
            if (b instanceof Double) {
                Double b_double = (Double) b;
                if (a_double == b_double) {
                    return Optional.empty();
                } else if (a_double > b_double) {
                    return Optional.of(a);
                } else {
                    return Optional.of(b);
                }
            } else if (b instanceof String) {
                String b_string = (String) b;
                double b_double = Double.parseDouble(b_string.replace(",", "."));

                if (a_double == b_double) {
                    return Optional.empty();
                } else if (a_double > b_double) {
                    return Optional.of(a);
                } else {
                    return Optional.of(b);
                }
            } else {
                throw new IllegalArgumentException();
            }
        } else if (a instanceof String) {
            String a_string = (String) a;
            double a_double = Double.parseDouble(a_string.replace(",", "."));

            if (b instanceof Double) {
                Double b_double = (Double) b;
                if (a_double == b_double) {
                    return Optional.empty();
                } else if (a_double > b_double) {
                    return Optional.of(a);
                } else {
                    return Optional.of(b);
                }
            } else if (b instanceof String) {
                String b_string = (String) b;
                double b_double = Double.parseDouble(b_string.replace(",", "."));

                if (a_double == b_double) {
                    return Optional.empty();
                } else if (a_double > b_double) {
                    return Optional.of(a);
                } else {
                    return Optional.of(b);
                }
            } else {
                throw new IllegalArgumentException();
            }
        } else {
            throw new IllegalArgumentException();
        }
    }
}

Q