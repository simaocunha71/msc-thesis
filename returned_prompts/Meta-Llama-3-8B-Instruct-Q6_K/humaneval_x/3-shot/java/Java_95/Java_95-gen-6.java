        if (dict.isEmpty()) {
            return false;
        }

        boolean lower = true;
        boolean upper = true;

        for (Map.Entry<Object, Object> entry : dict.entrySet()) {
            if (entry.getKey() instanceof String) {
                String key = (String) entry.getKey();
                if (!key.matches("^[a-z]+$")) {
                    lower = false;
                }
                if (!key.matches("^[A-Z]+$")) {
                    upper = false;
                }
            } else {
                return false;
            }
        }

        return lower || upper;
    }
}