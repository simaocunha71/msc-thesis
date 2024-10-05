    int i;
    for (i=txt.length()-1;i>=0;i--)
    if (txt[i]>='a' && txt[i]<='z' || txt[i]>='A' && txt[i]<='Z')
    return true;

    return false;
}



