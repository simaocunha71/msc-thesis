        if(dict.isEmpty()) return false;
        boolean lower = true, upper = true;
        for(String key : dict.keySet()){
            if(!key.equals(key.toLowerCase())){
                lower = false;
            }
            if(!key.equals(key.toUpperCase())){
                upper = false;
            }
            if(!lower && !upper) return false;
        }
        return true;
    }
}

