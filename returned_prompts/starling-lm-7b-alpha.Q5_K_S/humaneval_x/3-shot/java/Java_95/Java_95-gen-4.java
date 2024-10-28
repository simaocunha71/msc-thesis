        if (dict.isEmpty()) return false;

        Iterator<Map.Entry<Object, Object>> it = dict.entrySet().iterator();
        boolean all_lower = true;
        boolean all_upper = true;
        while (it.hasNext()) {
            Map.Entry<Object, Object> pair = it.next();
            if (pair.getKey() instanceof String) {
                String key = (String) pair.getKey();
                if (!key.equals(key.toLowerCase()) && !key.equals(key.toUpperCase())) {
                    all_lower = false;
                    all_upper = false;
                }
            }
        }
        return all_lower || all_upper;
    }
}

