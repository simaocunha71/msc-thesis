    int i;
    int l=txt.length();
    char chr=txt[l-1];
    if (l==0)
    return false;
    if (chr>='A' && chr<='Z')
    return true;
    if (chr>='a' && chr<='z')
    return true;
    return false;
}