        if (dict.isEmpty()) {
            return true;
        }
        boolean all_lower = true;
        boolean all_upper = true;
        for (Map.Entry<Object, Object> entry : dict.entrySet()) {
            String key = (String) entry.getKey();
            if (!key.toLowerCase().equals(key)) {
                all_lower = false;
            }
            if (!key.toUpperCase().equals(key)) {
                all_upper = false;
            }
        }
        return all_lower || all_upper;
    }
}

