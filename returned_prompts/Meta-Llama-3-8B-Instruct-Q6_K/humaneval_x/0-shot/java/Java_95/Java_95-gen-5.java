    if (dict.isEmpty()) {
        return false; // return false if the map is empty
    }

    boolean allLowerCase = true;
    boolean allUpperCase = true;

    for (Map.Entry<Object, Object> entry : dict.entrySet()) {
        String key = entry.getKey().toString();
        if (!allLowerCase && !allUpperCase) {
            break;
        }

        if (!key.matches("[a-z]+")) {
            allLowerCase = false;
        }
        if (!key.matches("[A-Z]+")) {
            allUpperCase = false;
        }
    }

    return allLowerCase || allUpperCase;
}
