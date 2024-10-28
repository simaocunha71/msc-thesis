        if (dict.isEmpty()) return false;
        boolean lowerCase = true;
        boolean upperCase = true;

        for (Map.Entry<Object, Object> entry : dict.entrySet()) {
            String key = entry.getKey().toString();
            if (Character.isUpperCase(key.charAt(0))) {
                lowerCase = false;
            } else if (Character.isLowerCase(key.charAt(0))) {
                upperCase = false;
            } else {
                return false;
            }
        }
        return lowerCase || upperCase;
    }
}

