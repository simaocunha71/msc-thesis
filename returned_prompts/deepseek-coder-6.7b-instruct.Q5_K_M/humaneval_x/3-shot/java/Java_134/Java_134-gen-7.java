        if(txt.length() == 0){
            return false;
        }
        if(txt.charAt(txt.length()-1) > 64 && txt.charAt(txt.length()-1) < 91 || 
           txt.charAt(txt.length()-1) > 96 && txt.charAt(txt.length()-1) < 123){
            if(txt.length() == 1){
                return true;
            }
            if(txt.charAt(txt.length()-2) == ' '){
                return true;
            }
        }
        return false;
    }
}

