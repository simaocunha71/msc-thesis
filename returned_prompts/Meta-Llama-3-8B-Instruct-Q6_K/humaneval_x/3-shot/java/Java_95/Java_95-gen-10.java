        if (dict.isEmpty()) return false;

        boolean isLower = true;
        boolean isUpper = true;

        for (Map.Entry<Object, Object> entry : dict.entrySet()) {
            if (!(entry.getKey() instanceof String)) return false;
            String key = (String) entry.getKey();
            if (!key.equals(key.toLowerCase())) isUpper = false;
            if (!key.equals(key.toUpperCase())) isLower = false;
        }
        return isLower || isUpper;
    }
}

