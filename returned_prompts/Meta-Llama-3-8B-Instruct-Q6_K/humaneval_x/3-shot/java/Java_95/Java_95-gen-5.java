        if (dict.isEmpty()) {
            return false;
        }

        boolean upperCase = true;
        boolean lowerCase = true;

        for (Map.Entry<Object, Object> entry : dict.entrySet()) {
            String key = entry.getKey().toString();
            if (!key.equals(key.toUpperCase()) && !key.equals(key.toLowerCase())) {
                return false;
            }
            if (!key.equals(key.toUpperCase())) {
                upperCase = false;
            }
            if (!key.equals(key.toLowerCase())) {
                lowerCase = false;
            }
        }
        return upperCase || lowerCase;
    }
}

