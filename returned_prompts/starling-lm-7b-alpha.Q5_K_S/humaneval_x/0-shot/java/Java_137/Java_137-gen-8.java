        if (a instanceof Integer && b instanceof Integer) {
            if (a.equals(b)) {
                return Optional.empty();
            } else if ((Integer) a > (Integer) b) {
                return Optional.of((Integer) a);
            } else {
                return Optional.of((Integer) b);
            }
        } else if (a instanceof Double && b instanceof Double) {
            if (a.equals(b)) {
                return Optional.empty();
            } else if ((Double) a > (Double) b) {
                return Optional.of((Double) a);
            } else {
                return Optional.of((Double) b);
            }
        } else if (a instanceof String && b instanceof String) {
            if (a.equals(b)) {
                return Optional.empty();
            } else if (a.toString().replace(",", ".").equals(b.toString().replace(",", "."))) {
                return Optional.empty();
            } else if (Double.parseDouble((String) a) > Double.parseDouble((String) b)) {
                return Optional.of((String) a);
            } else {
                return Optional.of((String) b);
            }
        }
        return Optional.empty();
    }
}














































































































































































































