    if(txt.size() == 0 || (!isalpha(txt[txt.size()-1]) && txt[txt.size()-1] != ' '))
        return false;

    for(int i = txt.size()-2; i >= 0; i--){
        if(txt[i] == ' ' && (isalpha(txt[i+1]) || txt[i+1] == ' '))
            return false;
        if(txt[i] != ' ' && (isalpha(txt[i+1]) || txt[i+1] == ' '))
            return true;
    }
    return false;
}


