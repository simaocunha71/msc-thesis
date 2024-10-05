        if(s.length() < 3){
            return false;
        }
        for(int i = 0; i < s.length() - 2; i++){
            String temp = s.substring(i, i+3);
            if(temp.charAt(0) == temp.charAt(1) || temp.charAt(1) == temp.charAt(2) || temp.charAt(0) == temp.charAt(2)){
                return false;
            }
        }
        return true;
    }
}
