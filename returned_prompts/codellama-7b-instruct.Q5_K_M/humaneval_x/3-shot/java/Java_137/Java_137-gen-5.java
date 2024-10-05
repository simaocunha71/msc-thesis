        if (a instanceof Float || a instanceof Double || b instanceof Float || b instanceof Double) {
            double a_as_double = Double.parseDouble(String.valueOf(a));
            double b_as_double = Double.parseDouble(String.valueOf(b));
            if (a_as_double > b_as_double) return Optional.of(a);
            else if (b_as_double > a_as_double) return Optional.of(b);
            else return Optional.empty();
        } else if (a instanceof String || b instanceof String) {
            String a_as_string = String.valueOf(a);
            String b_as_string = String.valueOf(b);
            if (a_as_string.contains(",") && b_as_string.contains(",")) {
                a_as_string = a_as_string.replaceAll(",", ".");
                b_as_string = b_as_string.replaceAll(",", ".");
            }
            double a_as_double = Double.parseDouble(a_as_string);
            double b_as_double = Double.parseDouble(b_as_string);
            if (a_as_double > b_as_double) return Optional.of(a);
            else if (b_as_double > a_as_double) return Optional.of(b);
            else return Optional.empty();
        } else if (a instanceof Integer || a instanceof Long || b instanceof Integer || b instanceof Long) {
            long a_as_long = Long.parseLong(String.valueOf(a));
            long b_as_long = Long.parseLong(String.valueOf(b));
            if (a_as_long > b_as_long) return Optional.of(a);
            else if (b_as_long > a_as_long) return Optional.of(b);
            else return Optional.empty();
        }
        return Optional.empty();
    }
}

