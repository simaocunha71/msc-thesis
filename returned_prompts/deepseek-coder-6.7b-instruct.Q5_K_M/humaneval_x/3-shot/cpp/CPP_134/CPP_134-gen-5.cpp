    if(txt.length() == 0 || (txt[txt.length()-1] >= 'A' && txt[txt.length()-1] <= 'Z') || (txt[txt.length()-1] >= 'a' && txt[txt.length()-1] <= 'z')){
        int i = txt.length()-2;
        while(i >= 0 && txt[i] == ' ') i--;
        return i >= 0 && txt[i] != ' ';
    }
    return false;
}


