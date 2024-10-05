        if (dict.isEmpty()) return false;

        boolean isLower = true;
        boolean isUpper = true;

        for (Map.Entry<Object, Object> entry : dict.entrySet()) {
            if (!isLower && !isUpper) return false;

            String key = entry.getKey().toString();
            if (!key.equals(key.toLowerCase())) {
                isLower = false;
            }
            if (!key.equals(key.toUpperCase())) {
                isUpper = false;
            }
        }

        return isLower || isUpper;
    }
}

