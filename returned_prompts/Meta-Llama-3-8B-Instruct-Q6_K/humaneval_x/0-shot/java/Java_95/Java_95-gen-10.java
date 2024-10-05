    if (dict.isEmpty()) {
        return false;
    }

    boolean allLower = true;
    boolean allUpper = true;

    for (Map.Entry<Object, Object> entry : dict.entrySet()) {
        String key = entry.getKey().toString();
        if (!key.isEmpty()) {
            if (!Character.isUpperCase(key.charAt(0))) {
                allUpper = false;
            }
            if (!Character.isLowerCase(key.charAt(0))) {
                allLower = false;
            }
        }
    }

    return allLower || allUpper;
}

