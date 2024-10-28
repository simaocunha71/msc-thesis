    if(dict.isEmpty()) {
        return false;
    }
    boolean isLower = true;
    boolean isUpper = true;
    for (Map.Entry<Object, Object> entry : dict.entrySet()) {
        String key = entry.getKey().toString();
        if(key.matches(".*[A-Z].*")) {
            isUpper = false;
        }
        if(key.matches(".*[a-z].*")) {
            isLower = false;
        }
        if(!isLower && !isUpper) {
            break;
        }
    }
    return isLower || isUpper;
}
