    int i,j,length;
    length=s.length();
    if (length<3)
    return false;
    for (i=0;i<length-2;i++)
    {
        if (s[i]==s[i+1] && s[i+1]==s[i+2])
        return false;
    }
    return true;
}



