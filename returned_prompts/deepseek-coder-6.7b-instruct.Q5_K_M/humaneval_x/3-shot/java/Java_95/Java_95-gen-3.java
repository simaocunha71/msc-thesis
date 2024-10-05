        if(dict.isEmpty()) return false;

        boolean allLower = true;
        boolean allUpper = true;

        for(Object key : dict.keySet()){
            if(!(key instanceof String)) return false;

            String strKey = (String) key;

            for(char c : strKey.toCharArray()){
                if(Character.isUpperCase(c)) allLower = false;
                if(Character.isLowerCase(c)) allUpper = false;
            }
        }
        return allLower || allUpper;
    }
}

