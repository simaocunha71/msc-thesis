        if (a.equals(b)) return Optional.empty();

        Double a_double = convertToDouble(a);
        Double b_double = convertToDouble(b);

        if (a_double == null || b_double == null) return Optional.empty();

        if (a_double > b_double) return Optional.of(a);
        else return Optional.of(b);
    }

    private Double convertToDouble(Object o) {
        if (o instanceof Double) return (Double) o;
        if (o instanceof Float) return (double) (Float) o;
        if (o instanceof Integer) return (double) (Integer) o;
        if (o instanceof Long) return (double) (Long) o;
        if (o instanceof String) {
            String str = (String) o;
            str = str.replace(',', '.');
            try {
                return Double.parseDouble(str);
            } catch (NumberFormatException e) {
                return null;
            }
        }
        return null;
    }
}