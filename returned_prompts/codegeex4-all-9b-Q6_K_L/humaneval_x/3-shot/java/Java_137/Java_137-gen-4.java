        double a_double;
        double b_double;
        try {
            a_double = Double.parseDouble(a.toString());
        } catch (Exception e) {
            return Optional.empty();
        }
        try {
            b_double = Double.parseDouble(b.toString());
        } catch (Exception e) {
            return Optional.empty();
        }

        if (a_double > b_double) {
            return Optional.of(a);
        } else if (a_double < b_double) {
            return Optional.of(b);
        } else {
            return Optional.empty();
        }
    }
}

