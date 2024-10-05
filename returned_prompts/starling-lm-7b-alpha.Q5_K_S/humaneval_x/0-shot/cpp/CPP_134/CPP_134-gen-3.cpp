    int len = txt.length();
    if(len==0)
    return false;
    if(txt[len-1]>='0' && txt[len-1]<='9' || txt[len-1]>='a' && txt[len-1]<='z' || txt[len-1]>='A' && txt[len-1]<='Z'){
        if(txt[len-1]==txt[len-1])
        return true;
    }
    else if(txt[len-1]==' ')
    return false;
    int i=