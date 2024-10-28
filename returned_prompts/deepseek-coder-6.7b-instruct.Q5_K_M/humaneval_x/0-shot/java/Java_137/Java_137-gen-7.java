        if (a instanceof String && b instanceof String) {
            String a1 = (String) a;
            String b1 = (String) b;
            a1 = a1.replace(",", ".");
            b1 = b1.replace(",", ".");
            if (Double.parseDouble(a1) > Double.parseDouble(b1)) {
                return Optional.of(a);
            }
            if (Double.parseDouble(b1) > Double.parseDouble(a1)) {
                return Optional.of(b);
            }
        }

        if (a instanceof String && (b instanceof Integer || b instanceof Float || b instanceof Double)) {
            String a1 = (String) a;
            a1 = a1.replace(",", ".");
            if (Double.parseDouble(a1) > Double.parseDouble(b.toString())) {
                return Optional.of(a);
            }
        }

        if ((a instanceof Integer || a instanceof Float || a instanceof Double) && b instanceof String) {
            String b1 = (String) b;
            b1 = b1.replace(",", ".");
            if (Double.parseDouble(b1) > Double.parseDouble(a.toString())) {
                return Optional.of(b);
            }
        }

        if (a instanceof Integer && b instanceof Integer) {
            if ((int) a > (int) b) {
                return Optional.of(a);
            }
            if ((int) b > (int) a) {
                return Optional.of(b);
            }
        }

        if (a instanceof Float && b instanceof Float) {
            if ((float) a > (float) b) {
                return Optional.of(a);
            }
            if ((float) b > (float) a) {
                return Optional.of(b);
            }
        }

        if (a instanceof Double && b instanceof Double) {
            if ((double) a > (double) b) {
                return Optional.of(a);
            }
            if ((double) b > (double) a) {
                return Optional.of(b);
           