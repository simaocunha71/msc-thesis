    if (dict.isEmpty()) {
        return false;
    }

    boolean allLower = true;
    boolean allUpper = true;

    for (Map.Entry<Object, Object> entry : dict.entrySet()) {
        String key = entry.getKey().toString();
        if (!Character.isLetter(key.charAt(0))) {
            return false;
        }
        for (int i = 0; i < key.length(); i++) {
            char c = key.charAt(i);
            if (!Character.isLetter(c)) {
                return false;
            }
            if (Character.isUpperCase(c)) {
                allLower = false;
            } else if (Character.isLowerCase(c)) {
                allUpper = false;
            }
        }
    }
    return allLower || allUpper;
}
