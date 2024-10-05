        if(dict.size() == 0) return false;

        for(Object key : dict.keySet()) {
            if(key instanceof String) {
                String keyStr = (String) key;
                if(!keyStr.equals(keyStr.toLowerCase()) && !keyStr.equals(keyStr.toUpperCase()))
                    continue A;
            } else return false;
        }
        return true;
    }
}
