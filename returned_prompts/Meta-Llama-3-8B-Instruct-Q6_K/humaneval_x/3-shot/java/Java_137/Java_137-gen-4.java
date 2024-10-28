        if (a instanceof Integer && b instanceof Integer) {
            return (Integer) a.compareTo((Integer) b) > 0 ?
                    Optional.of(a) : (Integer) a.compareTo((Integer) b) < 0 ?
                    Optional.of(b) : Optional.empty();
        } else if (a instanceof Double && b instanceof Double) {
            return (Double) a.compareTo((Double) b) > 0 ?
                    Optional.of(a) : (Double) a.compareTo((Double) b) < 0 ?
                    Optional.of(b) : Optional.empty();
        } else if (a instanceof String && b instanceof String) {
            String strA = a.toString().replaceAll(",", "");
            String strB = b.toString().replaceAll(",", "");
            return strA.compareTo(strB) > 0 ?
                    Optional.of(a) : strA.compareTo(strB) < 0 ?
                    Optional.of(b) : Optional.empty();
        } else if (a instanceof Integer && b instanceof Double) {
            return (Double) b.compareTo((double) a) > 0 ?
                    Optional.of(b) : Optional.empty();
        } else if (a instanceof Double && b instanceof Integer) {
            return (Double) a.compareTo((double) b) > 0 ?
                    Optional.of(a) : Optional.empty();
        } else if (a instanceof Integer && b instanceof String) {
            String strB = b.toString().replaceAll(",", "");
            return (Double) strB.compareTo((double) a) > 0 ?
                    Optional.of(b) : Optional.empty();
        } else if (a instanceof String && b instanceof Integer) {
            String strA = a.toString().replaceAll(",", "");
            return (Double) strA.compareTo((double) b) > 0 ?
                    Optional.of(a) : Optional.empty();
        } else if (a instanceof Double && b instanceof String) {
            String strB = b.toString().replaceAll(",", "");
            return (Double) a.compareTo((Double) strB) > 0 ?
                    Optional.of(a) : (Double) a.compareTo((Double) strB) < 0 ?
                    Optional.of(b) : Optional.empty();
        } else if (a instanceof String && b instanceof Double) {
            String strA = a.toString().replaceAll(",", "");
            return (Double) strA.compareTo((double) b) > 0 ?
                    Optional.of(a) : Optional.empty();
        }
        return Optional.empty();
    }
}

