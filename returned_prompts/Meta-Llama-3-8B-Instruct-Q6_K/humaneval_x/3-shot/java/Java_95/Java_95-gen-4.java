        if (dict.isEmpty()) {
            return false;
        }
        String key;
        for (Map.Entry<Object, Object> entry : dict.entrySet()) {
            key = entry.getKey().toString();
            if (!key.equals(key.toLowerCase()) && !key.equals(key.toUpperCase())) {
                return false;
            }
        }
        return true;
    }
}

