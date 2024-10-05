        double a_double = 0.0;
        double b_double = 0.0;

        if (a instanceof Double) {
            a_double = (Double) a;
        } else if (a instanceof String) {
            a_double = Double.parseDouble((String) a.replace(',', '.'));
        }

        if (b instanceof Double) {
            b_double = (Double) b;
        } else if (b instanceof String) {
            b_double = Double.parseDouble((String) b.replace(',', '.'));
        }

        if (a_double > b_double) {
            return Optional.of(a);
        } else if (b_double > a_double) {
            return Optional.of(b);
        } else {
            return Optional.empty();
        }

    }
}

