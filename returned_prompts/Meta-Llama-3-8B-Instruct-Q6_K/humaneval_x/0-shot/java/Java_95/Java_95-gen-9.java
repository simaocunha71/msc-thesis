    if(dict.isEmpty()) return false;

    boolean allLower = true;
    boolean allUpper = true;

    for(Object key : dict.keySet()) {
        if(key instanceof String) {
            String keyStr = (String) key;
            if(!keyStr.equals(keyStr.toLowerCase())) {
                allLower = false;
            }
            if(!keyStr.equals(keyStr.toUpperCase())) {
                allUpper = false;
            }
        } else {
            return false;
        }
    }

    return allLower || allUpper;
}