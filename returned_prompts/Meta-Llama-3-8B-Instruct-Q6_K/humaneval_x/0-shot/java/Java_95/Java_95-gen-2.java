    if(dict.isEmpty()) {
        return false;
    }

    boolean allLower = true;
    boolean allUpper = true;

    for (Map.Entry<Object, Object> entry : dict.entrySet()) {
        String key = String.valueOf(entry.getKey());
        if (!key.equals(key.toLowerCase())) {
            allLower = false;
        }
        if (!key.equals(key.toUpperCase())) {
            allUpper = false;
        }
    }

    return allLower || allUpper;
}
