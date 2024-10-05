        double a_double = Double.parseDouble(a.toString().replace(',', '.'));
        double b_double = Double.parseDouble(b.toString().replace(',', '.'));

        if (a_double > b_double) {
            return Optional.of(a);
        } else if (a_double < b_double) {
            return Optional.of(b);
        } else {
            return Optional.empty();
        }
    }
}

