        if (dict.isEmpty()) {
            return false;
        }
        boolean allLower = true;
        boolean allUpper = true;

        for (Map.Entry<Object, Object> entry : dict.entrySet()) {
            if (!(entry.getKey() instanceof String)) {
                return false;
            }
            String key = (String) entry.getKey();
            if (!Character.isUpperCase(key.charAt(0)) && !Character.isLowerCase(key.charAt(0))) {
                return false;
            }
            allLower &= Character.isLowerCase(key.charAt(0));
            allUpper &= Character.isUpperCase(key.charAt(0));
        }
        return allLower || allUpper;
    }
}

