        boolean all_lower = true;
        boolean all_upper = true;
        for (Object key : dict.keySet()) {
            if (key instanceof String) {
                char first_char = ((String) key).charAt(0);
                if (Character.isUpperCase(first_char)) {
                    all_lower = false;
                }
                if (Character.isLowerCase(first_char)) {
                    all_upper = false;
                }
            } else {
                return false;
            }
        }
        return all_lower || all_upper;
    }
}

