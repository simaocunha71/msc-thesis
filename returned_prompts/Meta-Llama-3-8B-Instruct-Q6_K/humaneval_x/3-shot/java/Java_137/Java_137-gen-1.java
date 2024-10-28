        if (a instanceof Integer && b instanceof Integer) {
            int ai = (int) a;
            int bi = (int) b;
            if (ai > bi) {
                return Optional.of(a);
            } else if (ai < bi) {
                return Optional.of(b);
            } else {
                return Optional.empty();
            }
        } else if (a instanceof Double && b instanceof Double) {
            double ad = (double) a;
            double bd = (double) b;
            if (ad > bd) {
                return Optional.of(a);
            } else if (ad < bd) {
                return Optional.of(b);
            } else {
                return Optional.empty();
            }
        } else if (a instanceof String && b instanceof String) {
            String as = (String) a;
            String bs = (String) b;
            double ad = Double.parseDouble(as.replace(',', '.'));
            double bd = Double.parseDouble(bs.replace(',', '.'));
            if (ad > bd) {
                return Optional.of(a);
            } else if (ad < bd) {
                return Optional.of(b);
            } else {
                return Optional.empty();
            }
        } else {
            throw new RuntimeException("Invalid inputs");
        }
    }
}

