        if (dict.isEmpty()) return false;

        boolean all_lower = true;
        boolean all_upper = true;

        for (Object key : dict.keySet()) {
            if (!(key instanceof String)) return false;
            String key_str = (String) key;
            all_lower = all_lower && key_str.equals(key_str.toLowerCase());
            all_upper = all_upper && key_str.equals(key_str.toUpperCase());
        }
        return all_lower || all_upper;
    }
}

