    if(txt.empty())
        return false;
    if(isalpha(txt[txt.size()-1])){
        if(txt.size()==1 || !isalpha(txt[txt.size()-2]))
            return true;
    }
    return false;
}


