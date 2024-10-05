        if (dict.size() == 0) return false;

        Object first_key = dict.keySet().iterator().next();
        if (first_key instanceof String) {
            for (Object key : dict.keySet()) {
                if (!((String)key).equals(((String)key).toLowerCase()) &&
                        !((String)key).equals(((String)key).toUpperCase())) return false;
            }
        } else {
            return false;
        }
        return true;
    }
}

