        if(dict.size()==0) return false;
        boolean lower = true, upper = true;

B:
        for(Object key: dict.keySet()){
            if(!(key instanceof String)) {
                lower = false; upper = false;
            }

C:
            if(!(key.toString().equals(key.toString().toLowerCase()))){
                lower = false;
            }

D:
            if(!(key.toString().equals(key.toString().toUpperCase()))){
                upper = false;
            }
        }

E:
        return lower || upper;
    }
}

*/

