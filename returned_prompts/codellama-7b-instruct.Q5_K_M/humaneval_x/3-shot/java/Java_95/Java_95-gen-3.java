        if (dict.isEmpty()) return false;

        boolean is_all_lower = true;
        boolean is_all_upper = true;

        for (Object key : dict.keySet()) {
            if (!(key instanceof String)) return false;
            String key_string = (String) key;
            if (!(key_string.equals(key_string.toLowerCase()) || key_string.equals(key_string.toUpperCase()))) return false;
            if (!key_string.equals(key_string.toLowerCase())) is_all_lower = false;
            if (!key_string.equals(key_string.toUpperCase())) is_all_upper = false;
        }
        return is_all_lower || is_all_upper;
    }
}

