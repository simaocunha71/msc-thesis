    if(txt[txt.length()-1] >= 'a' && txt[txt.length()-1] <= 'z' || txt[txt.length()-1] >= 'A' && txt[txt.length()-1] <= 'Z' && txt[txt.length()-1] != ' '){
        return true;
    }else{
        return false;
    }
}
