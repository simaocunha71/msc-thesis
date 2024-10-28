        if (dict.isEmpty()) return false;

        String first_key = dict.keySet().iterator().next().toString();
        boolean is_all_upper = first_key.equals(first_key.toUpperCase());
        boolean is_all_lower = first_key.equals(first_key.toLowerCase());

        for (Object key : dict.keySet()) {
            String key_string = key.toString();
            if (is_all_upper && !key_string.equals(key_string.toUpperCase())) return false;
            if (is_all_lower && !key_string.equals(key_string.toLowerCase())) return false;
        }
        return true;
    }
}

