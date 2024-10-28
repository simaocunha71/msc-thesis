        boolean all_lower = true;
        boolean all_upper = true;

        for (Object key : dict.keySet()) {
            String key_str = key.toString();
            if (key_str.length() == 0) continue;

            if (Character.isUpperCase(key_str.charAt(0))) all_lower = false;
            if (Character.isLowerCase(key_str.charAt(0))) all_upper = false;
        }
        return (all_lower || all_upper);
    }
}

