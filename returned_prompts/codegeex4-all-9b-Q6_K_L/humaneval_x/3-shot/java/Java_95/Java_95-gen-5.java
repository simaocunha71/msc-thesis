        if (dict.size() == 0) return false;
        boolean isLower = true;
        boolean isUpper = true;
        for (Object key : dict.keySet()) {
            if (!(key instanceof String)) return false;
            String keyString = (String) key;
            isLower = isLower && keyString.equals(keyString.toLowerCase());
            isUpper = isUpper && keyString.equals(keyString.toUpperCase());
        }
        return isLower || isUpper;
    }
}

