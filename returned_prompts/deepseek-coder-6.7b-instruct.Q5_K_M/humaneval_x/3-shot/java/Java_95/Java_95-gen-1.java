        boolean lower = true;
        boolean upper = true;

        for(Map.Entry<Object, Object> entry: dict.entrySet()){
            if(!(entry.getKey() instanceof String)) {
                return false;
            }
            String key = (String) entry.getKey();
            if(Character.isLowerCase(key.charAt(0))) {
                upper = false;
            }
            else if(Character.isUpperCase(key.charAt(0))) {
                lower = false;
            }
            else {
                return false;
            }
        }

        return lower || upper;
    }
}

