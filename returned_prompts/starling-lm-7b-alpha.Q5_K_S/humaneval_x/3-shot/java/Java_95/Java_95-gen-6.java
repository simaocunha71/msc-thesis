        Set<Object> keys = dict.keySet();
        int count_lower = 0;
        int count_upper = 0;
        for (Object key : keys) {
            if (key instanceof String) {
                String string_key = (String)key;
                if (string_key.equals(string_key.toLowerCase())) count_lower += 1;
                if (string_key.equals(string_key.toUpperCase())) count_upper += 1;
            }
        }
        return count_lower == keys.size() || count_upper == keys.size();
    }
}

