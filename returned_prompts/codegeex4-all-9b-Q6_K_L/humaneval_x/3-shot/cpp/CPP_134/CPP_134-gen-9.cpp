    int i;
    int len=txt.length();
    if (len==0)
    return false;
    char chr=txt[len-1];
    if ((chr>='a' && chr<='z') || (chr>='A' && chr<='Z'))
    return true;
    return false;
}

