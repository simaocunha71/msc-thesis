        Set<Object> keys = dict.keySet();
        Iterator<Object> it = keys.iterator();
        boolean all_lower_case = true;
        boolean all_upper_case = true;

        while (it.hasNext()) {
            Object key = it.next();
            if (key instanceof String) {
                String key_string = (String) key;
                if (!key_string.equalsIgnoreCase(key_string.toLowerCase())) {
                    all_lower_case = false;
                }
                if (!key_string.equalsIgnoreCase(key_string.toUpperCase())) {
                    all_upper_case = false;
                }
            } else {
                all_lower_case = false;
                all_upper_case = false;
                break;
            }
        }
        return all_lower_case || all_upper_case;
    }
}

