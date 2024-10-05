        if (dict.isEmpty()) return false;
        boolean isAllUpper = true;
        boolean isAllLower = true;
        for (Object key : dict.keySet()) {
            if (key instanceof String) {
                String keyStr = (String) key;
                if (keyStr.equals(keyStr.toUpperCase())) {
                    isAllLower = false;
                }
                else if (keyStr.equals(keyStr.toLowerCase())) {
                    isAllUpper = false;
                }
                else {
                    return false;
                }
            }
            else {
                return false;
            }
        }
        return !isAllLower && !isAllUpper;
    }
}

