        if (a instanceof Integer && b instanceof Integer) {
            int a_int = (int) a;
            int b_int = (int) b;
            return Optional.ofNullable(a_int > b_int ? a : b);
        } else if (a instanceof Float && b instanceof Float) {
            float a_float = (float) a;
            float b_float = (float) b;
            return Optional.ofNullable(a_float > b_float ? a : b);
        } else if (a instanceof String && b instanceof String) {
            String a_string = (String) a;
            String b_string = (String) b;
            return Optional.ofNullable(Double.parseDouble(a_string) > Double.parseDouble(b_string) ? a : b);
        }
        return Optional.empty();
    }
}

