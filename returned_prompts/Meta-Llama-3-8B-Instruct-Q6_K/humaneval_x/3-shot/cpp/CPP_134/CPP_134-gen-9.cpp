    if(txt.length()==0)
    return false;
    if(txt[txt.length()-1]==' ')
    return false;
    if(isalpha(txt[txt.length()-1]))
    return true;
    return false;
}