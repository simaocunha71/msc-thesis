        if (a.getClass()  !=  b.getClass()) {
            throw new IllegalArgumentException("Arguments must be of the same type.");
        }

        if (a instanceof Integer && b instanceof Integer) {
            return (Integer)a > (Integer)b ? Optional.of(a) : Optional.empty();
        } else if (a instanceof Double && b instanceof Double) {
            return (Double)a > (Double)b ? Optional.of(a) : Optional.empty();
        } else if (a instanceof String && b instanceof String) {
            return ((String)a).compareTo((String)b) > 0 ? Optional.of(a) : Optional.empty();
        } else {
            throw new IllegalArgumentException("Unsupported type: " + a.getClass().getName());
        }
    }
}

