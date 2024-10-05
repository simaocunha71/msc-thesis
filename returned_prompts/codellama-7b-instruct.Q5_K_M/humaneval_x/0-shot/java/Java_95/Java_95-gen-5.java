        if(dict.size() == 0) return false;
        boolean allLower = true;
        boolean allUpper = true;
        for(Object key : dict.keySet()) {
            if(key instanceof String) {
                String s = (String)key;
                if(!s.equals(s.toLowerCase()) && !s.equals(s.toUpperCase())) {
                    allLower = false;
                    allUpper = false;
                    break A;
                }
                if(s.equals(s.toLowerCase())) {
                    if(allUpper) {
                        allUpper = false;
                        break;
                    }
                } else {
                    if(allLower) {
                        allLower = false;
                        break;
                    }
                }
            } else {
                allLower = false;
                allUpper = false;
                break;
            }
        }
        return allLower || allUpper;
    }
}
