        if (dict.size() == 0) {
            return false;
        }
        boolean allUpper = true;
        boolean allLower = true;
        for (Map.Entry<Object, Object> entry : dict.entrySet()) {
            if (entry.getKey() instanceof String) {
                String s = (String) entry.getKey();
                if (!s.equals(s.toLowerCase())) {
                    allLower = false;
                }
                if (!s.equals(s.toUpperCase())) {
                    allUpper = false;
                }
            }
        }
        return (allLower || allUpper);
    }
}
