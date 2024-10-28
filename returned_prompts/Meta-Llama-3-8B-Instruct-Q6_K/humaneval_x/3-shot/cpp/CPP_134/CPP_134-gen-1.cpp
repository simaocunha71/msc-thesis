    int i;
    if (txt.length()==0)
    return false;
    for (i=txt.length()-2;i>=0;i--)
    if (txt[i]==' ')
    {
        if (isalpha(txt[i+1]))
        return true;
    }
    return isalpha(txt[txt.length()-1]);
}


