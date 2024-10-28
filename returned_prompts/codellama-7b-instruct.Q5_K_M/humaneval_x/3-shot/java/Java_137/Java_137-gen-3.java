        if (a instanceof Double || b instanceof Double) {
            Double a_double = Double.parseDouble(a.toString());
            Double b_double = Double.parseDouble(b.toString());
            if (a_double > b_double) return Optional.of(a);
            else if (b_double > a_double) return Optional.of(b);
            else return Optional.empty();
        }

        if (a instanceof Integer || b instanceof Integer) {
            Integer a_int = Integer.parseInt(a.toString());
            Integer b_int = Integer.parseInt(b.toString());
            if (a_int > b_int) return Optional.of(a);
            else if (b_int > a_int) return Optional.of(b);
            else return Optional.empty();
        }

        if (a.toString().equals(b.toString())) return Optional.empty();
        else return Optional.of(b);
    }
}

