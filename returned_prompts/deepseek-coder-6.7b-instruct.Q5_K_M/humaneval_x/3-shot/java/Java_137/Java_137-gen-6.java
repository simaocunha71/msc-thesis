        double doubleA = Double.MIN_VALUE;
        double doubleB = Double.MIN_VALUE;

        if(a instanceof Integer) {
            doubleA = (Integer) a;
        } else if(a instanceof Double) {
            doubleA = (Double) a;
        } else if(a instanceof String) {
            doubleA = Double.parseDouble((String) a);
        }

        if(b instanceof Integer) {
            doubleB = (Integer) b;
        } else if(b instanceof Double) {
            doubleB = (Double) b;
        } else if(b instanceof String) {
            doubleB = Double.parseDouble((String) b);
        }

        if(doubleA > doubleB) {
            return Optional.of(a);
        } else if(doubleA < doubleB) {
            return Optional.of(b);
        }

        return Optional.empty();
     }
}

