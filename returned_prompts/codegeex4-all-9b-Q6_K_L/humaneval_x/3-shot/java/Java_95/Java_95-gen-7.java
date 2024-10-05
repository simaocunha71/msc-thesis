        if (dict.isEmpty()) return false;
        boolean isUpper = true;
        boolean isLower = true;
        for (Object key : dict.keySet()) {
            if (!key.toString().equals(key.toString().toLowerCase())) isLower = false;
            if (!key.toString().equals(key.toString().toUpperCase())) isUpper = false;
        }
        return isLower || isUpper;
    }
}

