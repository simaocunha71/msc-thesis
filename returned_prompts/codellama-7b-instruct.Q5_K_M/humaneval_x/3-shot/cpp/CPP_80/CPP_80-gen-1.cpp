    int i,j;
    if (s.length()<3)
    return false;
    for (i=0;i<s.length()-1;i++)
    for (j=i+1;j<s.length();j++)
    if (s[i]==s[j])
    return false;
    return true;
}



