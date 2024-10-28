        if(dict.size() == 0){
            return false;
        }
        boolean allLower = true;
        boolean allUpper = true;
        for(Object key : dict.keySet()){
            if(!(key instanceof String)){
                return false;
            }
            String strKey = (String) key;
            for(char c : strKey.toCharArray()){
                if(Character.isLowerCase(c)){
                    allUpper = false;
                }
                if(Character.isUpperCase(c)){
                    allLower = false;
                }
            }
            if(!allLower && !allUpper){
                return false;
            }
            allLower = true;
            allUpper = true;
        }
        return true;
    }
}

