    int len=s.length();
    if (len<3)
    return false;
    if (len==3)
    return true;
    int i;
    for (i=0;i<len-2;i++)
    if (s[i]==s[i+1]&&s[i+1]==s[i+2])
    return false;
    return true;
}


