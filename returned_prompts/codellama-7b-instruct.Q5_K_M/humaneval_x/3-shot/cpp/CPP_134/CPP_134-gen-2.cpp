    if (txt.length()==0)
    return false;
    if (txt[txt.length()-1]>'a' && txt[txt.length()-1]<'z')
    return true;
    if (txt[txt.length()-1]>'A' && txt[txt.length()-1]<'Z')
    return true;
    return false;
}


