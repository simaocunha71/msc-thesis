        if (dict.isEmpty()) return false;

        boolean is_all_lower = true;
        boolean is_all_upper = true;

        for (Object key : dict.keySet()) {
            if (!(key instanceof String)) return false;
            String str = (String) key;
            if (!str.equalsIgnoreCase(str)) is_all_lower = false;
            if (str.equalsIgnoreCase(str)) is_all_upper = false;
        }
        return is_all_lower || is_all_upper;
    }
}

