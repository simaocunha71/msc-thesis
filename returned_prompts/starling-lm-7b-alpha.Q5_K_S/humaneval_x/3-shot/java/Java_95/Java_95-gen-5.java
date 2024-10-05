        if (dict.isEmpty()) {
            return true;
        }
        boolean all_lower = true;
        boolean all_upper = true;
        for (Object key : dict.keySet()) {
            if (key instanceof String) {
                String key_str = (String) key;
                if (!key_str.equals(key_str.toLowerCase())) {
                    all_lower = false;
                }
                if (!key_str.equals(key_str.toUpperCase())) {
                    all_upper = false;
                }
            } else {
                return false;
            }
        }
        return all_lower || all_upper;
    }
}

