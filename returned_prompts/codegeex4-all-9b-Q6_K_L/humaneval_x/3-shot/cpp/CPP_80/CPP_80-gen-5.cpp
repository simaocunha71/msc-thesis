    int i,j;
    
    if (s.length()<3)
    return false;

    for (i=0;i<s.length();i+=3)
    for (j=i+1;j<s.length();j++)
    {
        if (s[i]==s[j])
        return false;
    }
    return true;
}

