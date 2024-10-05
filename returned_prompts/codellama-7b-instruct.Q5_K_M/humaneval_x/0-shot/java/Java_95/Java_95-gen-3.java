        if (dict.isEmpty()) return false;

        Set<Object> keys = dict.keySet();
        for (Object key : keys) {
            if (!(key instanceof String)) {
                return false;
            }

            String keyString = (String) key;
            if (keyString.equalsIgnoreCase(keyString)) {
                continue;
            }

            boolean isLowerCase = false;
            boolean isUpperCase = false;
            for (int i = 0; i < keyString.length(); i++) {
                char c = keyString.charAt(i);
                if (Character.isLowerCase(c)) {
                    isLowerCase = true;
                } else if (Character.isUpperCase(c)) {
                    isUpperCase = true;
                } else {
                    return false;
                }
            }
            if (!isLowerCase && !isUpperCase) {
                return false;
            }
        }

        return true;
    }
}
