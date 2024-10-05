        if(s.length()<3){
            return false;
        }
        Set<Character> set = new HashSet<>();
        for(int i=0;i<s.length();i++){
            set.add(s.charAt(i));
        }
        if(set.size()!=s.length()){
            return true;
        }
        for(int i=0;i<s.length()-2;i++){
            Set<Character> temp = new HashSet<>();
            for(int j=i;j<i+3;j++){
                temp.add(s.charAt(j));
            }
            if(temp.size()!=3){
                break A;
            }
        }
        return false;
    }
}









































































```
