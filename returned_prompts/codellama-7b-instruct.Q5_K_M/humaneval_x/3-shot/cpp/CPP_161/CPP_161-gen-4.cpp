    int i;
    char c;
    string res="";
    for (i=0;i<s.length();i++)
    {
        c=s[i];
        if (c>='a' && c<='z')
        res+=c-32;
        if (c>='A' && c<='Z')
        res+=c+32;
        if (c>='0' && c<='9')
        res+=c;
    }
    if (res=="")
    return s;
    return res;
}


