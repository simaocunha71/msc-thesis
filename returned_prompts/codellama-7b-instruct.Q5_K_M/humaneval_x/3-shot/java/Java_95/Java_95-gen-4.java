        if (dict.isEmpty()) return true;
        boolean is_lower = true;
        boolean is_upper = true;

        for (Object key : dict.keySet()) {
            if (!(key instanceof String)) return false;

            String key_str = (String) key;

            if (key_str.toLowerCase().equals(key_str)) {
                if (!is_upper) return false;
            } else {
                if (!is_lower) return false;
            }

            is_lower = is_lower && Character.isLowerCase(key_str.charAt(0));
            is_upper = is_upper && Character.isUpperCase(key_str.charAt(0));
        }
        return true;
    }
}

