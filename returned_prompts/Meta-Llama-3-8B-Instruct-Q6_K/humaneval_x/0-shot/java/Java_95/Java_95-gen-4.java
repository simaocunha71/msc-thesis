    if(dict.isEmpty()) {
        return false;
    }
    boolean allLower = true;
    boolean allUpper = true;
    for(Map.Entry<Object, Object> entry : dict.entrySet()) {
        String key = entry.getKey().toString();
        if(Character.isUpperCase(key.charAt(0))) {
            allLower = false;
        } else if(Character.isLowerCase(key.charAt(0))) {
            allUpper = false;
        } else {
            return false;
        }
    }
    return allLower || allUpper;
}  // the function will return true if all keys are strings in lower case or all keys are strings in upper case, else return false. 

