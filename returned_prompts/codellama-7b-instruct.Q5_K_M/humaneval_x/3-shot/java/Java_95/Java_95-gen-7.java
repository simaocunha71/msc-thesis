        if (dict.isEmpty()) return false;
        boolean is_all_lower_case = true;
        boolean is_all_upper_case = true;
        for (Object key : dict.keySet()) {
            String key_str = (String) key;
            if (!key_str.matches("[a-zA-Z]+")) return false;
            if (!key_str.equals(key_str.toLowerCase()) && !key_str.equals(key_str.toUpperCase()))
                return false;
            if (!key_str.equals(key_str.toLowerCase())) is_all_upper_case = false;
            if (!key_str.equals(key_str.toUpperCase())) is_all_lower_case = false;
        }
        return is_all_lower_case || is_all_upper_case;
    }
}

