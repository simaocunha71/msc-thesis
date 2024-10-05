        if (a instanceof Integer && b instanceof Integer) {
            int intA = (int) a;
            int intB = (int) b;
            if (intA > intB) return Optional.of(a);
            else if (intA < intB) return Optional.of(b);
            else return Optional.empty();
        } else if (a instanceof Double && b instanceof Double) {
            double doubleA = (double) a;
            double doubleB = (double) b;
            if (doubleA > doubleB) return Optional.of(a);
            else if (doubleA < doubleB) return Optional.of(b);
            else return Optional.empty();
        } else if (a instanceof String && b instanceof String) {
            String strA = (String) a;
            String strB = (String) b;
            if (strA.compareTo(strB) > 0) return Optional.of(a);
            else if (strA.compareTo(strB) < 0) return Optional.of(b);
            else return Optional.empty();
        } else {
            throw new RuntimeException("Unsupported type");
        }
    }
}

