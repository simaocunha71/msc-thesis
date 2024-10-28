        if(dict.size() == 0){
            return false;
        }
        boolean lower = true;
        boolean upper = true;
        for(Object key : dict.keySet()){
            if(!(key instanceof String)){
                return false;
            }
            String k = (String) key;
            for(char c : k.toCharArray()){
                if(Character.isLowerCase(c)){
                    upper = false;
                } else if(Character.isUpperCase(c)){
                    lower = false;
                }
            }
            if(!lower && !upper){
                return false;
            }
            lower = true;
            upper = true;
        }
        return true;
    }
}

