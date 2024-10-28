    if(txt.length() == 0 || (txt[txt.length()-1] < 'A' || (txt[txt.length()-1] > 'Z' && txt[txt.length()-1] < 'a') || txt[txt.length()-1] > 'z'))
        return false;
    if(txt[txt.length()-2] == ' ' || txt.length() == 1)
        return true;
    return false;
}



