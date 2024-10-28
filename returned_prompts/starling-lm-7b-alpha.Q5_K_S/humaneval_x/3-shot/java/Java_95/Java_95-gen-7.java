        boolean all_lower_case = true;
        boolean all_upper_case = true;

        for (Object key : dict.keySet()) {
            String key_string = key.toString();
            if (!key_string.equalsIgnoreCase(key_string.toLowerCase())) {
                all_lower_case = false;
            }
            if (!key_string.equalsIgnoreCase(key_string.toUpperCase())) {
                all_upper_case = false;
            }
        }
        return all_lower_case || all_upper_case;
    }
}

