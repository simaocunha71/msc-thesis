        if (dict.isEmpty()) return false;

        for (Map.Entry<Object, Object> entry : dict.entrySet()) {
            if (entry.getKey().getClass() != String.class) return false;
            String key = (String) entry.getKey();
            if (key.matches("[A-Z]+") && !key.matches("[a-z]+")) return false;
            if (key.matches("[a-z]+") && !key.matches("[A-Z]+")) return false;
        }
        return true;
    }
}
