        double a_double = 0.0;
        double b_double = 0.0;

        try {
            a_double = Double.parseDouble(a.toString().replace(',', '.'));
        } catch (Exception e) {
            return Optional.empty();
        }

        try {
            b_double = Double.parseDouble(b.toString().replace(',', '.'));
        } catch (Exception e) {
            return Optional.empty();
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

