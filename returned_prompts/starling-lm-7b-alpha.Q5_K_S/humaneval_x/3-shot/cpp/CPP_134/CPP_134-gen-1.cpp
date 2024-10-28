    int i;
    for (i=txt.length()-1;i>=0;i--)
    if (txt[i]>='a' && txt[i]<='z')
    {
        if (i==txt.length()-1 || txt[i+1]==' ')
        return true;
    }
    return false;
}




