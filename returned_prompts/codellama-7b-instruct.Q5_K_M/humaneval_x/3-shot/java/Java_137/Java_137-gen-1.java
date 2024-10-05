        if (a instanceof String || b instanceof String) {
            String a_str = a.toString();
            String b_str = b.toString();
            try {
                double a_float = Double.parseDouble(a_str);
                double b_float = Double.parseDouble(b_str);
                if (a_float > b_float) return Optional.of(a);
                if (a_float < b_float) return Optional.of(b);
                return Optional.empty();

            } catch (NumberFormatException e) {
                throw new IllegalArgumentException("The given string is not a valid real number.");
            }
        } else {
            if (a instanceof Double || b instanceof Double) {
                double a_float = (Double) a;
                double b_float = (Double) b;
                if (a_float > b_float) return Optional.of(a);
                if (a_float < b_float) return Optional.of(b);
                return Optional.empty();
            } else {
                int a_int = (int) a;
                int b_int = (int) b;
                if (a_int > b_int) return Optional.of(a);
                if (a_int < b_int) return Optional.of(b);
                return Optional.empty();
            }
        }
    }
}

