        boolean isLower = true, isUpper = true;

        for(Map.Entry<Object, Object> entry : dict.entrySet()){
            if(!(entry.getKey() instanceof String)) {
                return false;
            }
            String key = (String) entry.getKey();

            for(char c : key.toCharArray()){
                if(Character.isLowerCase(c)){
                    isUpper = false;
                }else{
                    isLower = false;
                }
            }
        }
        return isLower || isUpper;
     }
}

