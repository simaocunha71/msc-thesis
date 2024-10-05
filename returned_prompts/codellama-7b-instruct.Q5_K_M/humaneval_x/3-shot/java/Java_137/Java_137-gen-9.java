        if (a instanceof Double || b instanceof Double) {
            Double a_double = (Double) (a instanceof Double ? a : Double.parseDouble(a.toString()));
            Double b_double = (Double) (b instanceof Double ? b : Double.parseDouble(b.toString()));
            if (a_double > b_double) return Optional.of(a);
            else if (a_double < b_double) return Optional.of(b);
            else return Optional.empty();
        }
        if (a instanceof Float || b instanceof Float) {
            Float a_float = (Float) (a instanceof Float ? a : Float.parseFloat(a.toString()));
            Float b_float = (Float) (b instanceof Float ? b : Float.parseFloat(b.toString()));
            if (a_float > b_float) return Optional.of(a);
            else if (a_float < b_float) return Optional.of(b);
            else return Optional.empty();
        }
        if (a instanceof Long || b instanceof Long) {
            Long a_long = (Long) (a instanceof Long ? a : Long.parseLong(a.toString()));
            Long b_long = (Long) (b instanceof Long ? b : Long.parseLong(b.toString()));
            if (a_long > b_long) return Optional.of(a);
            else if (a_long < b_long) return Optional.of(b);
            else return Optional.empty();
        }
        if (a instanceof Integer || b instanceof Integer) {
            Integer a_int = (Integer) (a instanceof Integer ? a : Integer.parseInt(a.toString()));
            Integer b_int = (Integer) (b instanceof Integer ? b : Integer.parseInt(b.toString()));
            if (a_int > b_int) return Optional.of(a);
            else if (a_int < b_int) return Optional.of(b);
            else return Optional.empty();
        }
        if (a instanceof String || b instanceof String) {
            String a_string = (String) (a instanceof String ? a : b.toString());
            String b_string = (String) (b instanceof String ? b : a.toString());