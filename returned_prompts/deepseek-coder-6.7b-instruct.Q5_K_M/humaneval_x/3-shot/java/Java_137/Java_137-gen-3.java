        if  (a instanceof Integer && b instanceof Integer) {
            return Optional.of(Math.max((Integer) a, (Integer) b));
        } else if  (a instanceof Double && b instanceof Double) {
            return Optional.of(Math.max((Double) a, (Double) b));
        } else if  (a instanceof String && b instanceof String) {
            return Optional.of(Math.max(Double.parseDouble((String) a), Double.parseDouble((String) b)));
        }

        return Optional.empty();
     }
}

