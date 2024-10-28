        if (dict.isEmpty()) {
            return true;
        }

        boolean is_all_lower = true;
        boolean is_all_upper = true;

        for (Object key : dict.keySet()) {
            if (!(key instanceof String)) {
                return false;
            }
            String key_str = (String) key;
            if (key_str.equals(key_str.toLowerCase())) {
                is_all_upper = false;
            } else if (key_str.equals(key_str.toUpperCase())) {
                is_all_lower = false;
            } else {
                return false;
            }
        }

        return is_all_lower || is_all_upper;
    }
}

