    int i;
    for (i=0;i<str.length();i++)
    if (str[i]>='A' && str[i]<='Z')
        str[i]+=32;
    else if (str[i]>='a' && str[i]<='z')
        str[i]-=32;
    return str;
}



