        double a_double = 0, b_double = 0;

        if (a instanceof String) {
            a_double = Double.parseDouble(((String) a).replace(',', '.'));
        } else {
            a_double = (double) a;
        }

        if (b instanceof String) {
            b_double = Double.parseDouble(((String) b).replace(',', '.'));
        } else {
            b_double = (double) b;
        }

        if (a_double == b_double) {
            return Optional.empty();
        } else if (a_double > b_double) {
            return Optional.of(a);
        } else {
            return Optional.of(b);
        }
    }
}

