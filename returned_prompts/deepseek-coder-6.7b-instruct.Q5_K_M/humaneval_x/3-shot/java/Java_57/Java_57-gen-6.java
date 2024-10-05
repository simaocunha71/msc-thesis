        if(l.size() < 2)
            return true;

        int dir = 0;
        for(int i = 0; i < l.size() - 1; i++){
            if(dir == 0){
                if(l.get(i) < l.get(i + 1)){
                    dir = 1;
                }else if(l.get(i) > l.get(i + 1)){
                    dir = -1;
                }
            }else if(dir == 1 && l.get(i) > l.get(i + 1)){
                return false;
            }else if(dir == -1 && l.get(i) < l.get(i + 1)){
                return false;
            }
        }
        return true;
     }
}

