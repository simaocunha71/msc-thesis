        if (dict.isEmpty()) return false;

        boolean allLower = true;
        boolean allUpper = true;

        for (Map.Entry<Object, Object> entry : dict.entrySet()) {
            if (!(entry.getKey() instanceof String)) return false;
            String key = (String) entry.getKey();
            if (!key.matches("^[a-z]+$")) allLower = false;
            if (!key.matches("^[A-Z]+$")) allUpper = false;
        }
        return allLower || allUpper;
    }
}

