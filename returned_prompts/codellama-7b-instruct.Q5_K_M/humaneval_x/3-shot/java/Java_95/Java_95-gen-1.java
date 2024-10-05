        if (dict.isEmpty()) return false;

        boolean all_lower = true;
        boolean all_upper = true;

        for (Map.Entry<Object, Object> e : dict.entrySet()) {
            String key = (String) e.getKey();

            if (!key.equalsIgnoreCase(key)) {
                all_lower = false;
            }

            if (all_lower && !key.equals(key.toLowerCase())) {
                all_upper = false;
            }
        }

        return all_lower || all_upper;
    }
}

