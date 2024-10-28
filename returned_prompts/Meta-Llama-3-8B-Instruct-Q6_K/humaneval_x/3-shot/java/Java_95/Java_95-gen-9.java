        if (dict.isEmpty()) return false;

        boolean allLower = true;
        boolean allUpper = true;

        for (Object key : dict.keySet()) {
            if (!(key instanceof String)) return false;

            if (!key.toString().matches("^[a-z]+$")) {
                allLower = false;
            }
            if (!key.toString().matches("^[A-Z]+$")) {
                allUpper = false;
            }
        }
        return allLower || allUpper;
    }
}

