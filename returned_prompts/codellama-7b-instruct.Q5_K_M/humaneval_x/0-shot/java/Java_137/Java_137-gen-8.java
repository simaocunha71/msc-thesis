        if (a instanceof Integer && b instanceof Integer) {
            if ((Integer) a > (Integer) b) {
                return Optional.of(a);
            } else if ((Integer) a ==