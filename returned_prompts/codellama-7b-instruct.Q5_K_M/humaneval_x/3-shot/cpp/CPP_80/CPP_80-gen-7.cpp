    if (s.length()<3)
    return false;
    int i,j;
    for (i=0;i<s.length()-2;i++)
    for (j=i+1;j<s.length()-1;j++)
    if (s[i]==s[j] && s[i+1]==s[j+1])
    return false;
    return true;
}


