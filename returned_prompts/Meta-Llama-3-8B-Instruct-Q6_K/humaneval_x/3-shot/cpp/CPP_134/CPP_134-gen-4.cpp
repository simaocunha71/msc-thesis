    if(txt.length() == 0) return false;
    if(txt[txt.length()-1] >= 'a' && txt[txt.length()-1] <= 'z' || txt[txt.length()-1] >= 'A' && txt[txt.length()-1] <= 'Z')
    {
        if(txt.find_first_not_of("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") != string::npos)
            return true;
    }
    return false;
}   


