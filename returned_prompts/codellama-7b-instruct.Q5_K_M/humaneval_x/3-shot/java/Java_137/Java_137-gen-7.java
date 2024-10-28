        if (a instanceof Double || a instanceof Float) {
            if (b instanceof Double || b instanceof Float) {
                double a_val = (Double) a;
                double b_val = (Double) b;
                if (a_val > b_val) return Optional.of(a);
                else if (a_val == b_val) return Optional.empty();
                else return Optional.of(b);
            } else if (b instanceof Integer || b instanceof Long) {
                double b_val = (Double) b;
                if (a instanceof Double) {
                    double a_val = (Double) a;
                    if (a_val > b_val) return Optional.of(a);
                    else return Optional.of(b);
                } else if (a instanceof Long) {
                    long a_val = (Long) a;
                    if (a_val > b_val) return Optional.of(a);
                    else return Optional.of(b);
                }
            }
        } else if (a instanceof Integer || a instanceof Long) {
            if (b instanceof Double || b instanceof Float) {
                double a_val = (Double) a;
                double b_val = (Double) b;
                if (a_val > b_val) return Optional.of(a);
                else if (a_val == b_val) return Optional.empty();
                else return Optional.of(b);
            } else if (b instanceof Integer || b instanceof Long) {
                long a_val = (Long) a;
                long b_val = (Long) b;
                if (a_val > b_val) return Optional.of(a);
                else if (a_val == b_val) return Optional.empty();
                else return Optional.of(b);
            }
        }
        return Optional.empty();
    }
}

