    int i,j;
    if (s.length()<3)
    return false;

    for (i=0;i<s.length();i++)
    for (j=i+1;j<s.length();j++)
    if (i+2<=j&&s[i]==s[i+1]&&s[i+1]==s[i+2])
    return false;

    return true;
}


