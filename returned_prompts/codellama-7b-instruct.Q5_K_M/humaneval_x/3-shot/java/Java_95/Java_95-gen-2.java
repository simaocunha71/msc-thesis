        if (dict.isEmpty()) return false;
        boolean all_lower = true;
        boolean all_upper = true;
        for (Object key : dict.keySet()) {
            if (!(key instanceof String)) return false;
            String key_string = (String) key;
            if (!key_string.equals(key_string.toLowerCase())) all_lower = false;
            if (!key_string.equals(key_string.toUpperCase())) all_upper = false;
        }
        return all_lower || all_upper;

    }
}

