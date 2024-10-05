public boolean checkDictCase(Map<Object, Object> dict) {
    if (dict.isEmpty()) {
        return false;
    }

    boolean allLowerCase = true;
    boolean allUpperCase = true;

    for (Object key : dict.keySet()) {
        if (!(key instanceof String)) {
            return false;
        }
        String keyStr = (String) key;
        if (!keyStr.equals(keyStr.toLowerCase())) {
            allLowerCase = false;
        }
        if (!keyStr.equals(keyStr.toUpperCase())) {
            allUpperCase = false;
        }
        if (!allLowerCase && !allUpperCase) {
            return false;
        }
    }

    return allLowerCase || allUpperCase;
}