    if (dict.isEmpty()) {
        return false;
    }

    boolean allLowerCase = true;
    boolean allUpperCase = true;

    for (Map.Entry<Object, Object> entry : dict.entrySet()) {
        String key = entry.getKey().toString();
        if (!key.equals(key.toLowerCase())) {
            allLowerCase = false;
        }
        if (!key.equals(key.toUpperCase())) {
            allUpperCase = false;
        }
    }

    return allLowerCase || allUpperCase;
}