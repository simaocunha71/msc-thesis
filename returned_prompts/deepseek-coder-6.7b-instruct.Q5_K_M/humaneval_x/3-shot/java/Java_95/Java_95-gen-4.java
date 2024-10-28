        if(dict.isEmpty()){
            return false;
        }

        boolean lower = true;
        boolean upper = true;

        for(Map.Entry<Object, Object> entry: dict.entrySet()){
            if(!(entry.getKey() instanceof String)){
                return false;
            }

            String key = (String)entry.getKey();
            for(char c: key.toCharArray()){
                if(Character.isUpperCase(c)){
                    lower = false;
                }
                if(Character.isLowerCase(c)){
                    upper = false;
                }
            }

            if(!lower && !upper){
                return false;
            }
        }

        return true;
     }
}

