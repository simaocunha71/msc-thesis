        if (dict.isEmpty()) {
            return false;
        }

        boolean allUpper = false;
        boolean allLower = false;

        for (Object key : dict.keySet()) {

            if (key.toString().toLowerCase().equals(key.toString())) {
                allLower = true;
            } else if (key.toString().toUpperCase().equals(key.toString())) {
                allUpper = true;
            } else {
                return false;
            }
        }

        return allLower || allUpper;
    }
}
