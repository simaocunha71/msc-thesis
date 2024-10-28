        double a, b;
        if (a instanceof String) {
            a = Double.parseDouble((String)a);
        } else {
            a = (double)a;
        }
        if (b instanceof String) {
            b = Double.parseDouble((String)b);
        } else {
            b = (double)b;
        }
        if (a > b) {
            return Optional.of(a);
        } else if (b > a) {
            return Optional.of(b);
        }
        return Optional.empty();
    }
}

