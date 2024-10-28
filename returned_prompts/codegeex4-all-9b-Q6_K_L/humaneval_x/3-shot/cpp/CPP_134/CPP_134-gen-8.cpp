    int i;
    for (i=0;i<txt.length();i++)
    if (txt[i]==' ')
    return false;
    char chr=txt[txt.length()-1];
    return (chr>='a' && chr<='z')||(chr>='A' && chr<='Z');
}