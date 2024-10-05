        if (a.getClass() == b.getClass()) {
            if (a instanceof Integer && (Integer) a > (Integer) b) {
                return Optional.of(a);
            } else if (a instanceof Double && (Double) a > (Double) b) {
                return Optional.of(a);
            } else if (a instanceof String) {
                String strA = ((String) a).replace(",", ".");
                String strB = ((String) b).replace(",", ".");
                if (Double.parseDouble(strA) > Double.parseDouble(strB)) {
                    return Optional.of(a);
                } else if (Double.parseDouble(strB) > Double.parseDouble(strA)) {
                    return Optional.of(b);
                }
            }
        } else {
            if ((a instanceof Integer || a instanceof Double) && (b instanceof Integer || b instanceof Double)) {
                if ((Double) a > (Double) b) {
                    return Optional.of(a);
                } else if ((Double) b > (Double) a) {
                    return Optional.of(b);
                }
            } else if (a instanceof String && b instanceof String) {
                String strA = ((String) a).replace(",", ".");
                String strB = ((String) b).replace(",", ".");
                if (Double.parseDouble(strA) > Double.parseDouble(strB)) {
                    return Optional.of(a);
                } else if (Double.parseDouble(strB) > Double.parseDouble(strA)) {
                    return Optional.of(b);
                }
            } else if ((a instanceof Integer || a instanceof Double) && (b instanceof String)) {
                if ((Double) a > Double.parseDouble(((String) b).replace(",", "."))) {
                    return Optional.of(a);
                }
            } else if ((b instanceof Integer || b instanceof Double) && (a instanceof String)) {
                if ((Double) b > Double.parseDouble(((String) a).replace(",", "."))) {
                    return Optional.of(b);
                }
            }
        }
        return Optional.