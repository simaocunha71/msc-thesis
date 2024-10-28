        if (dict == null || dict.isEmpty()) return false;
        boolean isUpper = false;
        boolean isLower = false;
        for (Map.Entry<Object, Object> entry : dict.entrySet()) {
            String key = (String) entry.getKey();
            if (key == null) continue;
            char c = key.charAt(0);
            if (c >= 'A' && c <= 'Z') {
                if (isLower) return false;
                isUpper = true;
            } else {
                if (isUpper) return false;
                isLower = true;
            }
        }
        return true;
    }
}
